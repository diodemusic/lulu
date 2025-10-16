from pyke import Region

from .._base_client import _BaseApiClient
from .._models.summoner_v4 import SummonerDTO


class SummonerEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> SummonerDTO:
        """Get a summoner by PUUID.

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `CurrentGameInfo:` pyke._models.summoner_v4.SummonerDTO
        """  # fmt: skip

        path = f"/lol/summoner/v4/summoners/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return SummonerDTO(**data)
