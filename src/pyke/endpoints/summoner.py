from pyke import Region

from .._base_client import _BaseApiClient
from ..models.summoner_v4 import SummonerDTO


class SummonerEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> SummonerDTO:
        """Get a summoner by PUUID.

        **Args:**  
            `region (Region):` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `SummonerDTO:` [SummonerDTO](/pyke/pyke/models/summoner_v4.html#SummonerDTO).
        """  # fmt: skip

        path = f"/lol/summoner/v4/summoners/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return SummonerDTO(**data)
