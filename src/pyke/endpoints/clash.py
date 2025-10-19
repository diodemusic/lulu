from pyke import Region

from .._base_client import _BaseApiClient
from ..models.clash_v1 import PlayerDto, TeamDto, TournamentDto


class ClashEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> list[PlayerDto]:
        """# Get players by puuid

        **Args:**  
            `region (Region):` Region to execute against (pyke.enums.region.Region).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `list[PlayerDto]:` List of pyke.models.clash_v1.PlayerDto objects.
        """  # fmt: skip

        path = f"/lol/clash/v1/players/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        players: list[PlayerDto] = []

        for player in data:
            players.append(PlayerDto(**player))

        return players

    def by_team_id(self, region: Region, team_id: str) -> TeamDto:
        """# Get team by ID

        **Args:**  
            `region (Region):` Region to execute against (pyke.enums.region.Region).  
            `team_id (str):` Team id of the clash team.  

        **Returns:**  
            `TeamDto:` pyke.models.clash_v1.TeamDto object.
        """  # fmt: skip

        path = f"/lol/clash/v1/teams/{team_id}"
        data = self._client._region_request(region=region, path=path)

        return TeamDto(**data)

    def tournaments(self, region: Region) -> list[TournamentDto]:
        """# Get all active or upcoming tournaments

        **Args:**  
            `region (Region):` Region to execute against (pyke.enums.region.Region).  

        **Returns:**  
            `list[TournamentDto]:` pyke.models.clash_v1.TournamentDto
        """  # fmt: skip

        path = "/lol/clash/v1/tournaments"
        data = self._client._region_request(region=region, path=path)

        tournaments: list[TournamentDto] = []

        for tournament in data:
            tournaments.append(TournamentDto(**tournament))

        return tournaments

    def tournament_by_team_id(self, region: Region, team_id: str) -> TournamentDto:
        """# Get tournament by team ID

        **Args:**  
            `region (Region):` Region to execute against (pyke.enums.region.Region).  
            `team_id (str):` Team id of the clash team.  

        **Returns:**  
            `TournamentDto:` pyke.models.clash_v1.TournamentDto object.
        """  # fmt: skip

        path = "/lol/clash/v1/tournaments"
        path = f"/lol/clash/v1/tournaments/by-team/{team_id}"
        data = self._client._region_request(region=region, path=path)

        return TournamentDto(**data)

    def tournament_by_tournament_id(
        self, region: Region, tournament_id: int
    ) -> TournamentDto:
        """# Get tournament by ID

        **Args:**  
            `region (Region):` Region to execute against (pyke.enums.region.Region).  
            `tournament_id (str):` Tournement id of the clash.  

        **Returns:**  
            `TournamentDto:` pyke.models.clash_v1.TournamentDto object.
        """  # fmt: skip

        path = f"/lol/clash/v1/tournaments/{tournament_id}"
        data = self._client._region_request(region=region, path=path)

        return TournamentDto(**data)
