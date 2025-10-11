from .._base_client import _BaseApiClient
from .._models.league_exp_v4 import LeagueEntryDTO
from ..enums.division import Division
from ..enums.queue import Queue
from ..enums.region import Region
from ..enums.tier import Tier


class LeagueExpEndpoint:
    def __init__(self, api_key: str | None):
        self._client = _BaseApiClient(api_key)

    def entries_by_queue_tier_division(
        self,
        region: Region,
        queue: Queue,
        tier: Tier,
        division: Division,
        page: int = 1,
    ) -> list[LeagueEntryDTO]:
        """Get all the league entries.

        Args:
            region (Region): Region to execute against.
            queue (Queue): Ranked queue enum.
            tier (Tier): Ranked tier enum.
            division (Division): Ranked tier enum.
            page (int, optional): Starts with page 1. Defaults to 1.

        Returns:
            list[LeagueEntryDTO]: Set of pyke.models.champion.LeagueEntryDTO objects.
        """

        path = f"/lol/league-exp/v4/entries/{queue.value}/{tier.value}/{division.value}"
        params = {"count": page}
        data = self._client._region_request(region=region, path=path, params=params)

        league_entries: list[LeagueEntryDTO] = []

        for league_entry in data:
            league_entries.append(LeagueEntryDTO(**league_entry))

        return league_entries
