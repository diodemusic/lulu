# lulu

from .endpoints.account import AccountEndpoint
from .endpoints.champion import ChampionEndpoint
from .endpoints.champion_mastery import ChampionMasteryEndpoint
from .endpoints.league_exp import LeagueExpEndpoint


class Lulu:
    """Main entrypoint for interacting with the Riot API."""

    def __init__(self, api_key: str | None):
        self.account = AccountEndpoint(api_key)
        self.champion_mastery = ChampionMasteryEndpoint(api_key)
        self.champion = ChampionEndpoint(api_key)
        self.league_exp = LeagueExpEndpoint(api_key)


# TODO Add Clash endpoint when a clash is active
