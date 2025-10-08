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
