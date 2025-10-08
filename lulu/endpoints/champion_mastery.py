from ..base_client import BaseApiClient

# from ..enums.continent import Continent
from ..enums.region import Region
from ..models.champion_mastery import ChampionMastery


class ChampionMasteryEndpoint:
    def __init__(self, api_key: str | None):
        self.client = BaseApiClient(api_key)

    def masteries_by_puuid(self, region: Region, puuid: str) -> list[ChampionMastery]:
        """Get all champion mastery entries sorted by number of champion points descending.

        Args:
            region (Region): Region to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.

        Returns:
            list[ChampionMastery]: List of lulu.models.champion_mastery.ChampionMastery objects.
        """

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
        data = self.client.region_request(region=region, path=path)

        champion_masteries: list[ChampionMastery] = []

        for champion_mastery in data:
            champion_masteries.append(ChampionMastery(**champion_mastery))

        return champion_masteries

    def by_puuid_and_champion_id(
        self, region: Region, puuid: str, champion_id: int
    ) -> ChampionMastery:
        """Get a champion mastery by puuid and champion ID.

        Args:
            region (Region): Region to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.
            champion_id (int): Champion ID for this entry.

        Returns:
            ChampionMastery: lulu.models.champion_mastery.ChampionMastery object.
        """

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
        data = self.client.region_request(region=region, path=path)

        return ChampionMastery(**data)

    def masteries_by_puuid_top(
        self, region: Region, puuid: str, count: int | None = None
    ) -> list[ChampionMastery]:
        """Get specified number of top champion mastery entries sorted by number of champion points descending.

        Args:
            region (Region): Region to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.
            count (int | None, optional): Number of entries to retrieve. defaults to 3.

        Returns:
            list[ChampionMastery]: List of lulu.models.champion_mastery.ChampionMastery objects.
        """

        path = f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"
        params = {"count": count}
        data = self.client.region_request(region=region, path=path, params=params)

        champion_masteries: list[ChampionMastery] = []

        for champion_mastery in data:
            champion_masteries.append(ChampionMastery(**champion_mastery))

        return champion_masteries
