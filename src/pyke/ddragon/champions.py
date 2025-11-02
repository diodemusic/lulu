from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class ChampionsData:
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

        return self._client._data_dragon_cdn_request(locale, "champion")

    def get_all_champions_full(self, locale: str) -> dict[str, Any]:
        """# Get all champions by locale

        **Example:**  
            `champions = ddragon.champions.get_all_champions_full(Locale.united_kingdom)`

        **Args:**  
            `locale (str)` Locale to use.  

        **Returns:**  
            `dict[str, any]`
        """  # fmt: skip

        return self._client._data_dragon_cdn_request(locale, "championFull")
