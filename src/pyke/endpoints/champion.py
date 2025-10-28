from pyke import Region

from .._base_client import _BaseApiClient
from ..models.champion_v3 import ChampionInfo


class ChampionEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def rotations(self, region: Region) -> ChampionInfo:
        """# Returns champion rotations, including free-to-play and low-level free-to-play rotations

        **Example:**  
            `rotations = api.champion.rotations(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `ChampionInfo` [ChampionInfo](/pyke/pyke/models/champion_v3.html#ChampionInfo).
        """  # fmt: skip

        path = "/lol/platform/v3/champion-rotations"
        data = self._client._region_request(region=region, path=path)

        return ChampionInfo(**data)
