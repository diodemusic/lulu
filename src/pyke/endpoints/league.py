from pyke import Division, Queue, Region, Tier

from .._base_client import _BaseApiClient
from ..models.league_v4 import LeagueEntryDTO, LeagueListDTO


class LeagueEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def challenger_leagues_by_queue(
        self,
        region: Region,
        queue: Queue,
    ) -> LeagueListDTO:
        """# Get the challenger league for given queue

        **Example:**  
            `leagues = api.league.challenger_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  

        **Returns:**  
            `list[LeagueListDTO]` List of [LeagueListDTO](/pyke/pyke/models/league_v4.html#LeagueListDTO).
        """  # fmt: skip

        path = f"/lol/league/v4/challengerleagues/by-queue/{queue.value}"
        data = self._client._region_request(region=region, path=path)

        return LeagueListDTO(**data)

    def by_puuid(self, region: Region, puuid: str) -> list[LeagueEntryDTO]:
        """# Get league entries in all queues for a given puuid

        **Example:**  
            `entries = api.league.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `list[LeagueEntryDTO]` List of [LeagueEntryDTO](/pyke/pyke/models/league_v4.html#LeagueEntryDTO).
        """  # fmt: skip

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
        """# Get all the league entries

        **Example:**  
            `entries = api.league.by_queue_tier_division(Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  
            `tier (Tier)` Ranked [Tier](/pyke/pyke.html#Tier).  
            `division (Division)` Ranked [Division](/pyke/pyke.html#Division).  
            `page (int, optional)` Starts with page 1. Defaults to 1.  

        **Returns:**  
            `list[LeagueEntryDTO]` List of [LeagueEntryDTO](/pyke/pyke/models/league_v4.html#LeagueEntryDTO).
        """  # fmt: skip

        path = f"/lol/league/v4/entries/{queue.value}/{tier.value}/{division.value}"
        params = {"page": page}
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
        """# Get the grandmaster league for given queue

        **Example:**  
            `leagues = api.league.grandmaster_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  

        **Returns:**  
            `LeagueListDTO` [LeagueListDTO](/pyke/pyke/models/league_v4.html#LeagueListDTO).
        """  # fmt: skip

        path = f"/lol/league/v4/grandmasterleagues/by-queue/{queue.value}"
        data = self._client._region_request(region=region, path=path)

        return LeagueListDTO(**data)

    def by_league_id(self, region: Region, league_id: str) -> LeagueListDTO:
        """# Get league with given ID, including inactive entries

        **Example:**  
            `leagues = api.league.by_league_id(Region.EUW, "some league id")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `league_id (str)` League id.  

        **Returns:**  
            `LeagueListDTO` [LeagueListDTO](/pyke/pyke/models/league_v4.html#LeagueListDTO).
        """  # fmt: skip

        path = f"/lol/league/v4/leagues/{league_id}"
        data = self._client._region_request(region=region, path=path)

        return LeagueListDTO(**data)

    def master_leagues_by_queue(
        self,
        region: Region,
        queue: Queue,
    ) -> LeagueListDTO:
        """# Get the master league for given queue

        **Example:**  
            `leagues = api.league.master_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  

        **Returns:**  
            `LeagueListDTO` [LeagueListDTO](/pyke/pyke/models/league_v4.html#LeagueListDTO).
        """  # fmt: skip

        path = f"/lol/league/v4/masterleagues/by-queue/{queue.value}"
        data = self._client._region_request(region=region, path=path)

        return LeagueListDTO(**data)
