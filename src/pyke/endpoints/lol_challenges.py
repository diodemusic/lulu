from pyke import Level, Region

from .._base_client import _BaseApiClient
from ..models.lol_challenges_v1 import (
    ApexPlayerInfoDto,
    ChallengeConfigInfoDto,
    PlayerInfoDto,
)


class ChallengesEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def config(self, region: Region) -> list[ChallengeConfigInfoDto]:
        """# List of all basic challenge configuration information (includes all translations for names and descriptions)

        **Example:**  
            `configs = api.lol_challenges.config(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `list[ChallengeConfigInfoDto]` List of [ChallengeConfigInfoDto](/pyke/pyke/models/lol_challenges_v1.html#ChallengeConfigInfoDto).
        """  # fmt: skip

        path = "/lol/challenges/v1/challenges/config"
        data = self._client._region_request(region=region, path=path)

        return [ChallengeConfigInfoDto(**challenge_config) for challenge_config in data]

    def percentiles(self, region: Region) -> dict[int, dict[int, dict[str, int]]]:
        """# Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it

        **Example:**  
            `percentiles = api.lol_challenges.percentiles(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `dict[int, dict[int, dict[str, int]]]` Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it.
        """  # fmt: skip

        path = "/lol/challenges/v1/challenges/percentiles"
        data = self._client._region_request(region=region, path=path)

        return data

    def config_by_challenge_id(
        self, region: Region, challenge_id: int
    ) -> ChallengeConfigInfoDto:
        """# Get challenge configuration (REST)

        **Example:**  
            `config = api.lol_challenges.config_by_challenge_id(Region.EUW, 123456)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `challenge_id (int)` Challenge id integer.  

        **Returns:**  
            `ChallengeConfigInfoDto` [ChallengeConfigInfoDto](/pyke/pyke/models/lol_challenges_v1.html#ChallengeConfigInfoDto).
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/config"
        data = self._client._region_request(region=region, path=path)

        return ChallengeConfigInfoDto(**data)

    def leaderboards_by_level(
        self, region: Region, level: Level, challenge_id: int
    ) -> list[ApexPlayerInfoDto]:
        """# Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER

        **Example:**  
            `players = api.lol_challenges.leaderboards_by_level(Region.EUW, Level.MASTER, 123456)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `level (Level)` Challenge [Level](/pyke/pyke.html#Level).  
            `challenge_id (int)` Challenge id integer.  

        **Returns:**  
            `list[ApexPlayerInfoDto]` List of [ApexPlayerInfoDto](/pyke/pyke/models/lol_challenges_v1.html#ApexPlayerInfoDto).
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level.value}"
        data = self._client._region_request(region=region, path=path)

        return [ApexPlayerInfoDto(**apex_player_info) for apex_player_info in data]

    def percentiles_by_challenge_id(
        self, region: Region, challenge_id: int
    ) -> dict[Level, int]:
        """# Dictionary of level to percentile of players who have achieved it

        **Example:**  
            `percentiles = api.lol_challenges.percentiles_by_challenge_id(Region.EUW, 123456)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `challenge_id (int)` Challenge id integer.  

        **Returns:**  
            `dict[Level, int]` Python dictionary {[Level](/pyke/pyke.html#Level): percentile of players who achieved the challenge}
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/percentiles"
        data = self._client._region_request(region=region, path=path)

        return data

    def by_puuid(self, region: Region, puuid: str) -> PlayerInfoDto:
        """# Returns player information with list of all progressed challenges (REST)

        **Example:**  
            `player_info = api.lol_challenges.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `PlayerInfoDto` [PlayerInfoDto](/pyke/pyke/models/lol_challenges_v1.html#PlayerInfoDto).
        """  # fmt: skip

        path = f"/lol/challenges/v1/player-data/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return PlayerInfoDto(**data)
