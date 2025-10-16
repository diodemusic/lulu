# pyke

from ._base_client import _BaseApiClient
from .endpoints.account import AccountEndpoint
from .endpoints.challenges import ChallengesEndpoint
from .endpoints.champion import ChampionEndpoint
from .endpoints.champion_mastery import ChampionMasteryEndpoint
from .endpoints.clash import ClashEndpoint
from .endpoints.league import LeagueEndpoint
from .endpoints.league_exp import LeagueExpEndpoint
from .endpoints.match import MatchEndpoint
from .endpoints.spectator import SpectatorEndpoint
from .endpoints.status import StatusEndpoint
from .endpoints.summoner import SummonerEndpoint
from .endpoints.tournament import TournamentEndpoint
from .endpoints.tournament_stub import TournamentStubEndpoint


class Pyke:
    """Main entrypoint for interacting with the Riot API."""

    def __init__(self, api_key: str | None = None, log_url: bool = True):
        self._client = _BaseApiClient(api_key, log_url)

        self.account = AccountEndpoint(self._client)
        self.champion_mastery = ChampionMasteryEndpoint(self._client)
        self.champion = ChampionEndpoint(self._client)
        self.clash = ClashEndpoint(self._client)
        self.league_exp = LeagueExpEndpoint(self._client)
        self.league = LeagueEndpoint(self._client)
        self.challenges = ChallengesEndpoint(self._client)
        self.status = StatusEndpoint(self._client)
        self.match = MatchEndpoint(self._client)
        self.spectator = SpectatorEndpoint(self._client)
        self.summoner = SummonerEndpoint(self._client)
        self.tournament_stub = TournamentStubEndpoint(self._client)
        self.tournament = TournamentEndpoint(self._client)
