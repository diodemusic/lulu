from .._base_client import _BaseApiClient
from .._models.champion_v3 import ChampionInfo
from ..enums.region import Region


class ChampionEndpoint:
    def __init__(self, api_key: str | None):
        self._client = _BaseApiClient(api_key)

    def rotations(self, region: Region) -> ChampionInfo:
        """Returns champion rotations, including free-to-play and low-level free-to-play rotations.

        Args:
            region (Region): Region to execute against.

        Returns:
            ChampionInfo: pyke.models.champion.ChampionInfo object.
        """

        path = "/lol/platform/v3/champion-rotations"
        data = self._client._region_request(region=region, path=path)

        return ChampionInfo(**data)
