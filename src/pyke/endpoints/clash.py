from pyke import Region

from .._base_client import _BaseApiClient
from ..models.clash_v1 import PlayerDto, TeamDto, TournamentDto


class ClashEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> list[PlayerDto]:
        """# Get players by puuid

        **Example:**  
            `players = api.clash.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `list[PlayerDto]` List of [PlayerDto](/pyke/pyke/models/clash_v1.html#PlayerDto).
        """  # fmt: skip

        path = f"/lol/clash/v1/players/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        players: list[PlayerDto] = []

        for player in data:
            players.append(PlayerDto(**player))

        return players

    def by_team_id(self, region: Region, team_id: str) -> TeamDto:
        """# Get team by ID

        **Example:**  
            `team = api.clash.by_team_id(Region.EUW, "some team id")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `team_id (str)` Team id of the clash team.  

        **Returns:**  
            `TeamDto` [TeamDto](/pyke/pyke/models/clash_v1.html#TeamDto).
        """  # fmt: skip

        path = f"/lol/clash/v1/teams/{team_id}"
        data = self._client._region_request(region=region, path=path)

        return TeamDto(**data)

    def tournaments(self, region: Region) -> list[TournamentDto]:
        """# Get all active or upcoming tournaments

        **Example:**  
            `tournaments = api.clash.tournaments(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `list[TournamentDto]` List of [TournamentDto](/pyke/pyke/models/clash_v1.html#TournamentDto).
        """  # fmt: skip

        path = "/lol/clash/v1/tournaments"
        data = self._client._region_request(region=region, path=path)

        tournaments: list[TournamentDto] = []

        for tournament in data:
            tournaments.append(TournamentDto(**tournament))

        return tournaments

    def tournament_by_team_id(self, region: Region, team_id: str) -> TournamentDto:
        """# Get tournament by team ID

        **Example:**  
            `tournament = api.clash.tournament_by_team_id(Region.EUW, "some team id")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `team_id (str)` Team id of the clash team.  

        **Returns:**  
            `TournamentDto` [TournamentDto](/pyke/pyke/models/clash_v1.html#TournamentDto).
        """  # fmt: skip

        path = f"/lol/clash/v1/tournaments/by-team/{team_id}"
        data = self._client._region_request(region=region, path=path)

        return TournamentDto(**data)

    def tournament_by_tournament_id(
        self, region: Region, tournament_id: int
    ) -> TournamentDto:
        """# Get tournament by ID

        **Example:**  
            `tournament = api.clash.tournament_by_tournament_id(Region.EUW, 12345)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `tournament_id (str)` Tournement id of the clash.  

        **Returns:**  
            `TournamentDto` [TournamentDto](/pyke/pyke/models/clash_v1.html#TournamentDto).
        """  # fmt: skip

        path = f"/lol/clash/v1/tournaments/{tournament_id}"
        data = self._client._region_request(region=region, path=path)

        return TournamentDto(**data)
