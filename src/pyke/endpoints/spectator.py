from pyke import Region

from .._base_client import _BaseApiClient
from .._models.spectator_v5 import CurrentGameInfo


class SpectatorEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> CurrentGameInfo:
        """# Get current game information for the given puuid

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `CurrentGameInfo:` pyke._models.spectator_v5.CurrentGameInfo
        """  # fmt: skip

        path = f"/lol/spectator/v5/active-games/by-summoner/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return CurrentGameInfo(**data)
