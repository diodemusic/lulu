from __future__ import annotations

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
        self.api_key = api_key
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
        try:
            count = int(
                response.headers.get("X-App-Rate-Limit-Count", "0").split(":")[0]
            )
        except IndexError:
            count = 0

        return count

    def _get_limit(self, response: Response) -> int:
        try:
            limit = int(response.headers.get("X-App-Rate-Limit", "100").split(":")[0])
        except IndexError:
            limit = 0

        return limit

    def _print_url(self, response: Response, url: str) -> None:
        if not self.print_url:
            return

        count = self._get_count(response)
        limit = self._get_limit(response)
        print(f"({count}/{limit}) - {url}")

    def _calculate_time_to_wait(self, response: Response) -> float:
        limit = self._get_limit(response)
        try:
            time_frame = int(
                response.headers.get("X-App-Rate-Limit-Count", "unknown")
                .split(":")[1]
                .split(",")[0]
            )
        except IndexError:
            time_frame = 120

        return time_frame / limit

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
        except ValueError:
            raise exceptions.InternalServerError("Empty JSON response", 500)

    def _get(self, url: str, params: dict[Any, Any] = {}) -> Any:
        while True:
            headers = {"X-Riot-Token": self.api_key}
            start_time = time.perf_counter()
            response = requests.get(url, headers=headers, params=params, timeout=30)
            self._print_url(response, url)
            self._wait(response, start_time)
            code = response.status_code

            if code == 200:
                return self._response_json(response)
            elif code == 429:
                self._retry_after(response)
                continue
            elif (
                code == 502
            ):  # Temporary fix to deal with riots broken match-v5 endpoint
                print("502, retrying")
                time.sleep(10)
                continue

            raise self._status_code_registry.get(
                code,
                exceptions.UnknownError(
                    "Unexpected response, something has gone terribly wrong", code
                ),
            )

    def _continent_request(
        self, continent: Continent, path: str, params: dict[Any, Any] = {}
    ) -> Any:
        url = f"{self.CONTINENT_BASE.format(continent=continent.value)}{path}"
        return self._get(url, params)

    def _region_request(
        self, region: Region, path: str, params: dict[Any, Any] = {}
    ) -> Any:
        url = f"{self.REGION_BASE.format(region=region.value)}{path}"
        return self._get(url, params)
