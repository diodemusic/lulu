# pyke

from .endpoints.account import AccountEndpoint
from .endpoints.champion import ChampionEndpoint
from .endpoints.champion_mastery import ChampionMasteryEndpoint
from .endpoints.clash import ClashEndpoint
from .endpoints.league import LeagueEndpoint
from .endpoints.league_exp import LeagueExpEndpoint
from .endpoints.lol_challenges import LolChallengesEndpoint
from .endpoints.lol_rso_match import LolRsoMatchEndpoint
from .endpoints.lol_status import LolStatusEndpoint
from .endpoints.match import MatchEndpoint
from .endpoints.spectator import SpectatorEndpoint
from .endpoints.summoner import SummonerEndpoint
from .endpoints.tournament import TournamentEndpoint
from .endpoints.tournament_stub import TournamentStubEndpoint


class Pyke:
    """Main entrypoint for interacting with the Riot API."""

    def __init__(self, api_key: str | None):
        self.account = AccountEndpoint(api_key)
        self.champion_mastery = ChampionMasteryEndpoint(api_key)
        self.champion = ChampionEndpoint(api_key)
        self.clash = ClashEndpoint(api_key)
        self.league_exp = LeagueExpEndpoint(api_key)
        self.league = LeagueEndpoint(api_key)
        self.lol_challenges = LolChallengesEndpoint(api_key)
        self.lol_rso_match = LolRsoMatchEndpoint(api_key)
        self.lol_status = LolStatusEndpoint(api_key)
        self.match = MatchEndpoint(api_key)
        self.spectator = SpectatorEndpoint(api_key)
        self.summoner = SummonerEndpoint(api_key)
        self.tournament_stub = TournamentStubEndpoint(api_key)
        self.tournament = TournamentEndpoint(api_key)
