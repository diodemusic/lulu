from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class ChallengesData:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    def get_all_challenges(self, locale: str) -> dict[str, Any]:
        """# Get all challenges by locale

        **Example:**  
            `champions = ddragon.champions.get_all_champions(Locale.united_kingdom)`

        **Args:**  
            `locale (str)` Locale to use.  

        **Returns:**  
            `dict[str, any]`
        """  # fmt: skip

        return self._client._data_dragon_cdn_request(locale, "challenges")
