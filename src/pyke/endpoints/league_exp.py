from __future__ import annotations

from pyke import Division, Queue, Region, Tier

from .._base_client import _BaseApiClient
from ..models.league_exp_v4 import LeagueEntryDTO


class LeagueExpEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_queue_tier_division(
        self,
        region: Region,
        queue: Queue,
        tier: Tier,
        division: Division,
        page: int | None = None,
    ) -> list[LeagueEntryDTO]:
        """# Get all the league entries

        **Example:**  
        `entries = api.league_exp.by_queue_tier_division(Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  
            `tier (Tier)` Ranked [Tier](/pyke/pyke.html#Tier).  
            `division (Division)` Ranked [Division](/pyke/pyke.html#Division).  
            `page (int, optional)` Starts with page 1. Defaults to 1.  

        **Returns:**  
            `list[LeagueEntryDTO]` List of [LeagueEntryDTO](/pyke/pyke/models/league_exp_v4.html#LeagueEntryDTO).
        """  # fmt: skip

        path = f"/lol/league-exp/v4/entries/{queue.value}/{tier.value}/{division.value}"
        params = {"page": page}
        data = self._client._region_request(region=region, path=path, params=params)

        league_entries: list[LeagueEntryDTO] = []

        for league_entry in data:
            league_entries.append(LeagueEntryDTO(**league_entry))

        return league_entries
