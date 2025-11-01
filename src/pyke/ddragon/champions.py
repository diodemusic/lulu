from typing import Any

from pyke import Locale

from .._base_data_dragon_client import _BaseDataDragonClient


class ChampionsEndpoint:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    def get_all_champions(self, locale: Locale) -> dict[str, Any]:
        path = f"/cdn/{self._client.version}/data/{locale.value}/champion.json"
        data = self._client._data_dragon_request(path)

        return data
