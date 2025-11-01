from __future__ import annotations

import json
import logging
import time
from typing import Any

import requests
from requests import Response

from . import exceptions
from .enums.continent import Continent
from .enums.region import Region

logger = logging.getLogger(__name__)


class _BaseApiClient:  # pyright: ignore[reportUnusedClass]
    CONTINENT_BASE = "https://{continent}.api.riotgames.com"
    REGION_BASE = "https://{region}.api.riotgames.com"

    def __init__(
        self,
        api_key: str | None,
        smart_rate_limiting: bool,
        timeout: int,
        max_rate_limit_retries: int,
        max_server_error_retries: int,
    ) -> None:
        if api_key is None:
            raise ValueError("API key is required, please pass a valid Riot API key.")

        self.api_key = api_key
        self.session = requests.Session()
        self.smart_rate_limiting = smart_rate_limiting
        self.timeout = timeout
        self.max_rate_limit_retries = max_rate_limit_retries
        self.max_server_error_retries = max_server_error_retries
        self._status_code_registry = {
            400: exceptions.BadRequest("Bad request", 400),
            401: exceptions.Unauthorized("Unauthorized", 401),
            403: exceptions.Forbidden("Forbidden", 403),
            404: exceptions.DataNotFound("Data not found", 404),
            405: exceptions.MethodNotAllowed("Method not allowed", 405),
            415: exceptions.UnsupportedMediaType("Unsupported media type", 415),
            500: exceptions.InternalServerError("Internal server error", 500),
            502: exceptions.BadGateway("Bad gateway", 502),
            503: exceptions.ServiceUnavailable("Service unavailable", 503),
            504: exceptions.GatewayTimeout("Gateway timeout", 504),
        }

    def _get_count(self, response: Response) -> int:
        header_value = response.headers.get("X-App-Rate-Limit-Count")

        if not header_value:
            return 0

        parts = header_value.split(":")

        if len(parts) < 1 or not parts[0]:
            logger.warning(f"Invalid X-App-Rate-Limit-Count format: {header_value}")

            return 0

        try:
            return int(parts[0])
        except ValueError:
            logger.warning(f"Non-integer count in X-App-Rate-Limit-Count: {parts[0]}")

            return 0

    def _get_limit(self, response: Response) -> int:
        header_value = response.headers.get("X-App-Rate-Limit")

        if not header_value:
            return 100

        parts = header_value.split(":")

        if len(parts) < 1 or not parts[0]:
            logger.warning(f"Invalid X-App-Rate-Limit format: {header_value}")

            return 100

        try:
            return int(parts[0])
        except ValueError:
            logger.warning(f"Non-integer limit in X-App-Rate-Limit: {parts[0]}")

            return 100

    def _log_rate_limit(self, response: Response) -> None:
        count = self._get_count(response)
        limit = self._get_limit(response)
        logger.info(f"Rate limit: ({count}/{limit})")

    def _calculate_time_to_wait(self, response: Response) -> float:
        limit = self._get_limit(response)
        header_value = response.headers.get("X-App-Rate-Limit-Count")

        if not header_value:
            return 120 / limit

        comma_parts = header_value.split(",")

        if not comma_parts[0]:
            logger.warning(f"Invalid X-App-Rate-Limit-Count format: {header_value}")

            return 120 / limit

        colon_parts = comma_parts[0].split(":")

        if len(colon_parts) < 2 or not colon_parts[1]:
            logger.warning(
                f"Missing time_frame in X-App-Rate-Limit-Count: {header_value}"
            )

            return 120 / limit

        try:
            time_frame = int(colon_parts[1])

            return time_frame / limit
        except ValueError:
            logger.warning(
                f"Non-integer time_frame in X-App-Rate-Limit-Count: {colon_parts[1]}"
            )

            return 120 / limit

    def _wait(self, response: Response, start_time: float | None = None) -> None:
        if not self.smart_rate_limiting:
            return

        time_to_wait = self._calculate_time_to_wait(response)

        if start_time is not None:
            elapsed = time.perf_counter() - start_time
            remaining = time_to_wait - elapsed
        else:
            remaining = time_to_wait

        if remaining > 0:
            time.sleep(remaining)

    def _retry_after(self, response: Response) -> None:
        retry_after = int(response.headers.get("Retry-After", "120"))
        logger.warning(f"Rate limit exceeded, waiting {retry_after} seconds")
        time.sleep(retry_after)

    def _response_json(self, response: Response) -> Any:
        try:
            return response.json()
        except json.JSONDecodeError:
            raise exceptions.InternalServerError("Could not decode JSON", 500)
        except ValueError:
            raise exceptions.InternalServerError("Empty JSON response", 500)

    def _get(self, url: str, params: dict[Any, Any] | None = None) -> Any:
        rate_limit_retry_count = 0
        server_error_retry_count = 0

        while True:
            start_time = time.perf_counter()
            logging.info(url)
            headers = {"X-Riot-Token": self.api_key}

            try:
                response = self.session.get(
                    url, headers=headers, params=params, timeout=self.timeout
                )
            except requests.exceptions.Timeout:
                raise exceptions.RequestTimeout(
                    f"Request timed out after {self.timeout} seconds", 408
                )

            self._log_rate_limit(response)
            self._wait(response, start_time)
            code = response.status_code

            if code == 200:
                return self._response_json(response)

            elif code == 429:
                rate_limit_retry_count += 1
                logger.warning(
                    f"Rate limit retries: {rate_limit_retry_count}/{self.max_rate_limit_retries}"
                )

                if rate_limit_retry_count >= self.max_rate_limit_retries:
                    raise exceptions.RateLimitExceeded(
                        f"Rate limit exceeded after {self.max_rate_limit_retries} retries",
                        429,
                    )

                self._retry_after(response)
                continue

            elif code in (502, 503, 504):
                server_error_retry_count += 1
                logger.warning(
                    f"Server error {code}, retry {server_error_retry_count}/{self.max_server_error_retries}"
                )

                if server_error_retry_count >= self.max_server_error_retries:
                    raise self._status_code_registry.get(
                        code,
                        exceptions.UnknownError(
                            f"Server error {code} after {self.max_server_error_retries} retries",
                            code,
                        ),
                    )

                if code == 504:
                    wait_time = 10 * (2 ** (server_error_retry_count - 1))
                else:
                    wait_time = 5 * (2 ** (server_error_retry_count - 1))

                logger.warning(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)

                continue

            raise self._status_code_registry.get(
                code,
                exceptions.UnknownError(
                    "Unexpected response, something has gone terribly wrong", code
                ),
            )

    def _continent_request(
        self, continent: Continent, path: str, params: dict[Any, Any] | None = None
    ) -> Any:
        url = f"{self.CONTINENT_BASE.format(continent=continent.value)}{path}"

        return self._get(url, params)

    def _region_request(
        self, region: Region, path: str, params: dict[Any, Any] | None = None
    ) -> Any:
        url = f"{self.REGION_BASE.format(region=region.value)}{path}"

        return self._get(url, params)
