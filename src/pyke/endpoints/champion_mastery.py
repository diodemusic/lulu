from __future__ import annotations

from pyke import Region

from .._base_client import _BaseApiClient
from ..models.champion_mastery_v4 import ChampionMasteryDto


class ChampionMasteryEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def masteries_by_puuid(
        self, region: Region, puuid: str
    ) -> list[ChampionMasteryDto]:
        """# Get all champion mastery entries sorted by number of champion points descending

        **Example:**  
            `masteries = api.champion_mastery.masteries_by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `list[ChampionMasteryDto]` List of [ChampionMasteryDto](/pyke/pyke/models/champion_mastery_v4.html#ChampionMasteryDto).
        """  # fmt: skip

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return [ChampionMasteryDto(**champion_mastery) for champion_mastery in data]

    def by_puuid_and_champion_id(
        self, region: Region, puuid: str, champion_id: int
    ) -> ChampionMasteryDto:
        """# Get a champion mastery by puuid and champion ID

        **Example:**  
            `mastery = api.champion_mastery.by_puuid_and_champion_id(Region.EUW, "some puuid", 29)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  
            `champion_id (int)` Champion ID for this entry.  

        **Returns:**  
            `ChampionMasteryDto` [ChampionMasteryDto](/pyke/pyke/models/champion_mastery_v4.html#ChampionMasteryDto).
        """  # fmt: skip

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
        data = self._client._region_request(region=region, path=path)

        return ChampionMasteryDto(**data)

    def masteries_by_puuid_top(
        self, region: Region, puuid: str, count: int | None = None
    ) -> list[ChampionMasteryDto]:
        """# Get specified number of top champion mastery entries sorted by number of champion points descending

        **Example:**  
            `masteries = api.champion_mastery.masteries_by_puuid_top(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  
            `count (int | None, optional)` Number of entries to retrieve. defaults to 3.  

        **Returns:**  
            `list[ChampionMasteryDto]` List of [ChampionMasteryDto](/pyke/pyke/models/champion_mastery_v4.html#ChampionMasteryDto).
        """  # fmt: skip

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"
        params = {"count": count}
        data = self._client._region_request(region=region, path=path, params=params)

        return [ChampionMasteryDto(**champion_mastery) for champion_mastery in data]

    def score_by_puuid(self, region: Region, puuid: str) -> int:
        """# Get a player's total champion mastery score, which is the sum of individual champion mastery levels

        **Example:**  
            `score = api.champion_mastery.score_by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `int` Player's total champion mastery score.
        """  # fmt: skip

        path = f"/lol/champion-mastery/v4/scores/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return int(data)
