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

    def __init__(self, api_key: str | None, print_url: bool) -> None:
        self.api_key = api_key
        self.print_url = print_url
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

    def _print_url(self, response: Response, url: str) -> None:
        if self.print_url:
            count = response.headers.get("X-App-Rate-Limit-Count", "unknown").split(
                ":"
            )[0]
            limit = response.headers.get("X-App-Rate-Limit", "unknown").split(":")[0]
            print(f"({count}/{limit}) - {url}")

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
            response = requests.get(url, headers=headers, params=params, timeout=30)
            self._print_url(response, url)

            code = response.status_code

            if code == 200:
                return self._response_json(response)
            elif code == 429:
                self._retry_after(response)
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
