from pyke import Division, Queue, Region, Tier

from .._base_client import _BaseApiClient
from .._models.league_v4 import LeagueEntryDTO, LeagueListDTO


class LeagueEndpoint:
    def __init__(self, api_key: str | None):
        self._client = _BaseApiClient(api_key)

    def challenger_leagues_by_queue(
        self,
        region: Region,
        queue: Queue,
    ) -> LeagueListDTO:
        """Get the challenger league for given queue.

        Args:
            region (Region): Region to execute against (pyke.enums.region.Region).
            queue (Queue): Ranked queue type (pyke.enums.queue.Queue).

        Returns:
            LeagueListDTO: pyke.models.league_v4.LeagueListDTO object.
        """

        path = f"/lol/league/v4/challengerleagues/by-queue/{queue.value}"
        data = self._client._region_request(region=region, path=path)

        return LeagueListDTO(**data)

    def by_puuid(self, region: Region, puuid: str) -> list[LeagueEntryDTO]:
        """Get league entries in all queues for a given puuid.

        Args:
            region (Region): Region to execute against (pyke.enums.region.Region).
            puuid (str): Encrypted PUUID. Exact length of 78 characters.

        Returns:
            list[LeagueEntryDTO]: List of pyke.models.league_exp_v4.LeagueEntryDTO objects.
        """

        path = f"/lol/league/v4/entries/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        league_entries: list[LeagueEntryDTO] = []

        for league_entry in data:
            league_entries.append(LeagueEntryDTO(**league_entry))

        return league_entries

    def by_queue_tier_division(
        self,
        region: Region,
        queue: Queue,
        tier: Tier,
        division: Division,
        page: int = 1,
    ) -> list[LeagueEntryDTO]:
        """Get all the league entries.

        Args:
            region (Region): Region to execute against (pyke.enums.region.Region).
            queue (Queue): Ranked queue type (pyke.enums.queue.Queue).
            tier (Tier): Ranked tier (pyke.enums.tier.Tier).
            division (Division): Ranked division (pyke.enums.division.Division).
            page (int, optional): Starts with page 1. Defaults to 1.

        Returns:
            list[LeagueEntryDTO]: List of pyke.models.league_v4.LeagueEntryDTO objects.
        """

        path = f"/lol/league/v4/entries/{queue.value}/{tier.value}/{division.value}"
        params = {"count": page}
        data = self._client._region_request(region=region, path=path, params=params)

        league_entries: list[LeagueEntryDTO] = []

        for league_entry in data:
            league_entries.append(LeagueEntryDTO(**league_entry))

        return league_entries

    def grandmaster_leagues_by_queue(
        self,
        region: Region,
        queue: Queue,
    ) -> LeagueListDTO:
        """Get the grandmaster league for given queue.

        Args:
            region (Region): Region to execute against (pyke.enums.region.Region).
            queue (Queue): Ranked queue type (pyke.enums.queue.Queue).

        Returns:
            LeagueListDTO: pyke.models.league_v4.LeagueListDTO object.
        """

        path = f"/lol/league/v4/grandmasterleagues/by-queue/{queue.value}"
        data = self._client._region_request(region=region, path=path)

        return LeagueListDTO(**data)

    def by_league_id(self, region: Region, league_id: str) -> LeagueListDTO:
        path = f"/lol/league/v4/leagues/{league_id}"
        data = self._client._region_request(region=region, path=path)

        return LeagueListDTO(**data)
