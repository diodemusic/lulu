from pyke import Region

from .._base_client import _BaseApiClient
from ..models.spectator_v5 import CurrentGameInfo


class SpectatorEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> CurrentGameInfo:
        """# Get current game information for the given puuid

        **Example:**  
            ``

        **Args:**
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.

        **Returns:**
            `CurrentGameInfo` [CurrentGameInfo](/pyke/pyke/models/spectator_v5.html#CurrentGameInfo).
        """  # fmt: skip

        path = f"/lol/spectator/v5/active-games/by-summoner/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return CurrentGameInfo(**data)
