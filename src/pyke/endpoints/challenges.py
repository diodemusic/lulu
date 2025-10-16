from pyke import Level, Region

from .._base_client import _BaseApiClient
from .._models.challenges_v1 import (
    ApexPlayerInfoDto,
    ChallengeConfigInfoDto,
    PlayerInfoDto,
)


class ChallengesEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def config(self, region: Region) -> list[ChallengeConfigInfoDto]:
        """# List of all basic challenge configuration information (includes all translations for names and descriptions)

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  

        **Returns:**  
            `list[ChallengeConfigInfoDto]:` List of pyke._models.challenges_v1.ChallengeConfigInfoDto objects.
        """  # fmt: skip

        path = "/lol/challenges/v1/challenges/config"
        data = self._client._region_request(region=region, path=path)

        challenge_configs: list[ChallengeConfigInfoDto] = []

        for challenge_config in data:
            challenge_configs.append(ChallengeConfigInfoDto(**challenge_config))

        return challenge_configs

    def percentiles(self, region: Region) -> dict[int, dict[int, dict[str, int]]]:
        """# Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  

        **Returns:**  
            `dict[int, dict[int, dict[str, int]]]:` Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it.
        """  # fmt: skip

        path = "/lol/challenges/v1/challenges/percentiles"
        data = self._client._region_request(region=region, path=path)

        return data

    def config_by_challenge_id(
        self, region: Region, challenge_id: int
    ) -> ChallengeConfigInfoDto:
        """# Get challenge configuration (REST)

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `challenge_id (int):` Challenge id integer.  

        **Returns:**  
            `ChallengeConfigInfoDto:` pyke._models.challenges_v1.ChallengeConfigInfoDto object.
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/config"
        data = self._client._region_request(region=region, path=path)

        return ChallengeConfigInfoDto(**data)

    def leaderboards_by_level(
        self, region: Region, level: Level, challenge_id: int
    ) -> list[ApexPlayerInfoDto]:
        """# Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `level (Level):` Challenge level (pyke._enums.level.Level).  
            `challenge_id (int):` Challenge id integer.  

        **Returns:**  
            `list[ApexPlayerInfoDto]:` List of pyke._models.challenges_v1.ApexPlayerInfoDto objects.
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level.value}"
        data = self._client._region_request(region=region, path=path)

        apex_player_infos: list[ApexPlayerInfoDto] = []

        for apex_player_info in data:
            apex_player_infos.append(ApexPlayerInfoDto(**apex_player_info))

        return apex_player_infos

    def percentiles_by_challenge_id(
        self, region: Region, challenge_id: int
    ) -> dict[Level, int]:
        """# Dictionary of level to percentile of players who have achieved it

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `challenge_id (int):` Challenge id integer.  

        **Returns:**  
            `dict[Level, int]:` Python dictionary {pyke._enums.level.Level: percentile of players who achieved the challenge}
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/percentiles"
        data = self._client._region_request(region=region, path=path)

        return data

    def by_puuid(self, region: Region, puuid: str) -> PlayerInfoDto:
        """# Returns player information with list of all progressed challenges (REST)

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `PlayerInfoDto:` pyke._models.challenges_v1.PlayerInfoDto object.
        """  # fmt: skip

        path = f"/lol/challenges/v1/player-data/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return PlayerInfoDto(**data)
