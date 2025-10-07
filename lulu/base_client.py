from typing import Any

import requests

from .enums.continent import Continent


class BaseApiClient:
    CONTINENT_BASE = "https://{continent}.api.riotgames.com"

    def __init__(self, api_key: str | None):
        self.api_key = api_key

    def _get(self, url: str, params: dict[Any, Any] | None = None):
        print(url)

        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        return response.json()

    def continent_request(
        self, continent: Continent, path: str, params: dict[Any, Any] | None = None
    ):
        url = f"{self.CONTINENT_BASE.format(continent=continent.value)}{path}"
        return self._get(url, params)
