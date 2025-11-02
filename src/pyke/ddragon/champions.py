from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class ChampionsEndpoint:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    def get_all_champions(self, locale: str) -> dict[str, Any]:
        """# Get all champions by locale

        **Example:**  
            `champions = ddragon.champions.get_all_champions(Locale.united_kingdom)`

        **Args:**  
            `locale (str)` Locale to use.  

        **Returns:**  
            `dict[str, any]`
        """  # fmt: skip

        path = f"/cdn/{self._client.version}/data/{locale}/champion.json"
        data = self._client._data_dragon_request(path)

        return data

    def get_all_champions_full(self, locale: str) -> dict[str, Any]:
        """# Get all champions by locale

        **Example:**  
            `champions = ddragon.champions.get_all_champions_full(Locale.united_kingdom)`

        **Args:**  
            `locale (str)` Locale to use.  

        **Returns:**  
            `dict[str, any]`
        """  # fmt: skip

        path = f"/cdn/{self._client.version}/data/{locale}/championFull.json"
        data = self._client._data_dragon_request(path)

        return data
