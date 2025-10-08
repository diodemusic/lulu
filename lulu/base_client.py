from typing import Any

import requests

from . import exceptions
from .enums.continent import Continent


class BaseApiClient:
    CONTINENT_BASE = "https://{continent}.api.riotgames.com"

    def __init__(self, api_key: str | None):
        self.api_key = api_key

    def _get(self, url: str, params: dict[Any, Any] | None = None):
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers, params=params)
        rate_limit_count = (
            response.headers.get("X-App-Rate-Limit-Count", "")
            .split(",")[0]
            .replace(":", "/")
        )
        print(f"({rate_limit_count}) - {url}")
        code = response.status_code

        if code == 400:
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
            raise exceptions.RateLimitExceeded("Rate limit exceeded", 429)
        elif code == 500:
            raise exceptions.InternalServerError("Internal server error", 500)
        elif code == 502:
            raise exceptions.BadGateway("Bad gateway", 502)
        elif code == 503:
            raise exceptions.ServiceUnavailable("Service unavailable", 503)
        elif code == 504:
            raise exceptions.GatewayTimeout("Gateway timeout", 504)
        elif code == 200:
            return response.json()
        else:
            print("Uncaught exception")

        return response.json()

    def continent_request(
        self, continent: Continent, path: str, params: dict[Any, Any] | None = None
    ):
        url = f"{self.CONTINENT_BASE.format(continent=continent.value)}{path}"
        return self._get(url, params)
