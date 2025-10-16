from pyke import Region

from .._base_client import _BaseApiClient
from .._models.champion_mastery_v4 import ChampionMasteryDto


class ChampionMasteryEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def masteries_by_puuid(
        self, region: Region, puuid: str
    ) -> list[ChampionMasteryDto]:
        """# Get all champion mastery entries sorted by number of champion points descending

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `list[ChampionMasteryDto]:` List of pyke._models.champion_mastery_v4.ChampionMasteryDto objects.
        """  # fmt: skip

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        champion_masteries: list[ChampionMasteryDto] = []

        for champion_mastery in data:
            champion_masteries.append(ChampionMasteryDto(**champion_mastery))

        return champion_masteries

    def by_puuid_and_champion_id(
        self, region: Region, puuid: str, champion_id: int
    ) -> ChampionMasteryDto:
        """# Get a champion mastery by puuid and champion ID

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  
            `champion_id (int):` Champion ID for this entry.  

        **Returns:**  
            `ChampionMasteryDto:` pyke._models.champion_mastery_v4.ChampionMasteryDto object.
        """  # fmt: skip

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
        data = self._client._region_request(region=region, path=path)

        return ChampionMasteryDto(**data)

    def masteries_by_puuid_top(
        self, region: Region, puuid: str, count: int | None = None
    ) -> list[ChampionMasteryDto]:
        """# Get specified number of top champion mastery entries sorted by number of champion points descending

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  
            `count (int | None, optional):` Number of entries to retrieve. defaults to 3.  

        **Returns:**  
            `list[ChampionMasteryDTO]:` List of pyke._models.champion_mastery_v4.ChampionMasteryDTO objects.
        """  # fmt: skip

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"
        params = {"count": count}
        data = self._client._region_request(region=region, path=path, params=params)

        champion_masteries: list[ChampionMasteryDto] = []

        for champion_mastery in data:
            champion_masteries.append(ChampionMasteryDto(**champion_mastery))

        return champion_masteries

    def score_by_puuid(self, region: Region, puuid: str) -> int:
        """# Get a player's total champion mastery score, which is the sum of individual champion mastery levels

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `int:` Player's total champion mastery score.
        """  # fmt: skip

        path = f"/lol/champion-mastery/v4/scores/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return data
