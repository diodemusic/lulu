import time
from typing import Any

import requests

from . import exceptions
from ._enums.continent import Continent
from ._enums.region import Region


class _BaseApiClient:  # pyright: ignore[reportUnusedClass]
    CONTINENT_BASE = "https://{continent}.api.riotgames.com"
    REGION_BASE = "https://{region}.api.riotgames.com"

    def __init__(self, api_key: str | None, log_url: bool):
        self.api_key = api_key
        self.log_url = log_url

    def _get(self, url: str, params: dict[Any, Any] | None = None):
        while True:
            headers = {"X-Riot-Token": self.api_key}
            response = requests.get(url, headers=headers, params=params)

            if self.log_url:
                limit = response.headers.get("X-App-Rate-Limit", "unknown")
                count = response.headers.get("X-App-Rate-Limit-Count", "unknown")
                print(f"({count.split(':')[0]}/{limit.split(':')[0]}) - {url}")

            code = response.status_code

            if code == 200:
                try:
                    return response.json()
                except ValueError:
                    raise exceptions.InternalServerError("Empty JSON response", 500)

            elif code == 400:
                raise exceptions.BadRequest("Bad request", 400)
            elif code == 401:
                raise exceptions.Unauthorized("Unauthorized", 401)
            elif code == 403:
                raise exceptions.Forbidden("Forbidden", 403)
            elif code == 404:
                raise exceptions.DataNotFound("Data not found", 404)
            elif code == 405:
                raise exceptions.MethodNotAllowed("Method not allowed", 405)
            elif code == 415:
                raise exceptions.UnsupportedMediaType("Unsupported media type", 415)
            elif code == 429:
                retry_after = int(response.headers.get("Retry-After", "120"))
                print(f"Rate limit exceeded, waiting {retry_after} seconds")
                time.sleep(retry_after)
                continue
            elif code == 500:
                raise exceptions.InternalServerError("Internal server error", 500)
            elif code == 502:
                raise exceptions.BadGateway("Bad gateway", 502)
            elif code == 503:
                raise exceptions.ServiceUnavailable("Service unavailable", 503)
            elif code == 504:
                raise exceptions.GatewayTimeout("Gateway timeout", 504)
            else:
                raise exceptions.UnknownError(
                    "Unexpected response, something has gone terribly wrong", code
                )

    def _continent_request(
        self, continent: Continent, path: str, params: dict[Any, Any] | None = None
    ):
        url = f"{self.CONTINENT_BASE.format(continent=continent.value)}{path}"
        return self._get(url, params)

    def _region_request(
        self, region: Region, path: str, params: dict[Any, Any] | None = None
    ):
        url = f"{self.REGION_BASE.format(region=region.value)}{path}"
        return self._get(url, params)
