from pyke import Region

from .._base_client import _BaseApiClient
from .._models.challenges_v1 import ChallengeConfigInfoDto


class ChallengesEndpoint:
    def __init__(self, api_key: str | None):
        self._client = _BaseApiClient(api_key)

    def config(self, region: Region) -> list[ChallengeConfigInfoDto]:
        """List of all basic challenge configuration information (includes all translations for names and descriptions).

        Args:
            region (Region): Region to execute against (pyke.enums.region.Region).

        Returns:
            list[ChallengeConfigInfoDto]: List of pyke._models.challenges_v1.ChallengeConfigInfoDto objects.
        """

        path = "/lol/challenges/v1/challenges/config"
        data = self._client._region_request(region=region, path=path)

        challenge_configs: list[ChallengeConfigInfoDto] = []

        for challenge_config in data:
            challenge_configs.append(ChallengeConfigInfoDto(**challenge_config))

        return challenge_configs

    def percentiles(self, region: Region) -> dict[int, dict[int, dict[str, int]]]:
        """Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it.

        Args:
            region (Region): Region to execute against (pyke.enums.region.Region).

        Returns:
            dict[int, dict[int, dict[str, int]]]: Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it.
        """

        path = "/lol/challenges/v1/challenges/percentiles"
        data = self._client._region_request(region=region, path=path)

        return data
