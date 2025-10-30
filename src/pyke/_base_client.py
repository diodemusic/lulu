from __future__ import annotations

import json
import time
from typing import Any

import requests
from requests import Response

from . import exceptions
from .enums.continent import Continent
from .enums.region import Region


class _BaseApiClient:  # pyright: ignore[reportUnusedClass]
    CONTINENT_BASE = "https://{continent}.api.riotgames.com"
    REGION_BASE = "https://{region}.api.riotgames.com"

    def __init__(
        self,
        api_key: str | None,
        print_url: bool = True,
        smart_rate_limiting: bool = True,
    ) -> None:
        if api_key is None:
            raise ValueError("API key is required, please pass a valid Riot API key.")

        self.api_key = api_key
        self.session = requests.Session()
        self.print_url = print_url
        self.smart_rate_limiting = smart_rate_limiting
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
            print(f"Invalid X-App-Rate-Limit-Count format: {header_value}")

            return 0

        try:
            return int(parts[0])
        except ValueError:
            print(f"Non-integer count in X-App-Rate-Limit-Count: {parts[0]}")

            return 0

    def _get_limit(self, response: Response) -> int:
        header_value = response.headers.get("X-App-Rate-Limit")

        if not header_value:
            return 100

        parts = header_value.split(":")

        if len(parts) < 1 or not parts[0]:
            print(f"Invalid X-App-Rate-Limit format: {header_value}")

            return 100

        try:
            return int(parts[0])
        except ValueError:
            print(f"Non-integer limit in X-App-Rate-Limit: {parts[0]}")

            return 100

    def _print_url(self, response: Response, url: str) -> None:
        if not self.print_url:
            return

        count = self._get_count(response)
        limit = self._get_limit(response)
        print(f"({count}/{limit}) - {url}")

    def _calculate_time_to_wait(self, response: Response) -> float:
        limit = self._get_limit(response)
        header_value = response.headers.get("X-App-Rate-Limit-Count")

        if not header_value:
            return 120 / limit

        comma_parts = header_value.split(",")

        if not comma_parts[0]:
            print(f"Invalid X-App-Rate-Limit-Count format: {header_value}")

            return 120 / limit

        colon_parts = comma_parts[0].split(":")

        if len(colon_parts) < 2 or not colon_parts[1]:
            print(f"Missing time_frame in X-App-Rate-Limit-Count: {header_value}")

            return 120 / limit

        try:
            time_frame = int(colon_parts[1])

            return time_frame / limit
        except ValueError:
            print(f"Non-integer time_frame in X-App-Rate-Limit-Count: {colon_parts[1]}")

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
        print(f"Rate limit exceeded, waiting {retry_after} seconds")
        time.sleep(retry_after)

    def _response_json(self, response: Response) -> Any:
        try:
            return response.json()
        except json.JSONDecodeError:
            raise exceptions.InternalServerError("Could not decode JSON", 500)
        except ValueError:
            raise exceptions.InternalServerError("Empty JSON response", 500)

    def _get(self, url: str, params: dict[Any, Any] | None = None) -> Any:
        max_retries = 5
        retry_count = 0

        while True:
            headers = {"X-Riot-Token": self.api_key}
            start_time = time.perf_counter()

            try:
                response = self.session.get(
                    url, headers=headers, params=params, timeout=30
                )
            except requests.exceptions.Timeout:
                raise exceptions.RequestTimeout(
                    "Request timed out after 30 seconds", 408
                )

            self._print_url(response, url)
            self._wait(response, start_time)
            code = response.status_code

            if code == 200:
                return self._response_json(response)
            elif code == 429:
                retry_count += 1
                print(f"Rate limit retries: {retry_count}/{max_retries}")

                if retry_count >= max_retries:
                    raise exceptions.RateLimitExceeded(
                        f"Rate limit exceeded after {max_retries} retries", 429
                    )

                self._retry_after(response)

                continue
            elif code in (502, 503, 504):
                retry_count += 1
                print(f"Server error {code}, retry {retry_count}/{max_retries}")

                if retry_count >= max_retries:
                    raise self._status_code_registry.get(
                        code,
                        exceptions.UnknownError(
                            f"Server error {code} after {max_retries} retries", code
                        ),
                    )

                wait_time = 5 * (2 ** (retry_count - 1))
                print(f"Waiting {wait_time} seconds before retry...")
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
