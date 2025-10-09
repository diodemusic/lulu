from ..base_client import BaseApiClient
from ..enums.region import Region
from ..models.champion_v3 import ChampionInfo


class ChampionEndpoint:
    def __init__(self, api_key: str | None):
        self.client = BaseApiClient(api_key)

    def rotations(self, region: Region) -> ChampionInfo:
        """Returns champion rotations, including free-to-play and low-level free-to-play rotations.

        Args:
            region (Region): Region to execute against.

        Returns:
            ChampionInfo: pyke.models.champion.ChampionInfo object.
        """

        path = "/lol/platform/v3/champion-rotations"
        data = self.client.region_request(region=region, path=path)

        return ChampionInfo(**data)
