# pyke

from __future__ import annotations

from ._base_client import _BaseApiClient
from ._base_data_dragon_client import _BaseDataDragonClient
from .ddragon.challenges import ChallengesData

# Data dragon
from .ddragon.champions import ChampionsData
from .ddragon.versions import VersionsData

# Riot API
from .endpoints.account import AccountEndpoint
from .endpoints.champion import ChampionEndpoint
from .endpoints.champion_mastery import ChampionMasteryEndpoint
from .endpoints.clash import ClashEndpoint
from .endpoints.league import LeagueEndpoint
from .endpoints.league_exp import LeagueExpEndpoint
from .endpoints.lol_challenges import ChallengesEndpoint
from .endpoints.lol_status import StatusEndpoint
from .endpoints.match import MatchEndpoint
from .endpoints.spectator import SpectatorEndpoint
from .endpoints.summoner import SummonerEndpoint


class Pyke:
    """# Main entrypoint for interacting with the Riot API

    **Example:**  
        `api = Pyke("API_KEY")`

    **Args:**  
        `api_key (str | None)` Your Riot API key.  
        `smart_rate_limiting (bool, optional)` Automatically throttle requests to stay under rate limits. Defaults to True.  
        `timeout (int, optional)` Request timeout in seconds. Defaults to 60.  
        `max_rate_limit_retries (int, optional)` Maximum retry attempts for 429 rate limit errors. Defaults to 5.  
        `max_server_error_retries (int, optional)` Maximum retry attempts for 502/503/504 server errors. Defaults to 3.
    """  # fmt: skip

    def __init__(
        self,
        api_key: str | None,
        smart_rate_limiting: bool = True,
        timeout: int = 60,
        max_rate_limit_retries: int = 5,
        max_server_error_retries: int = 3,
    ) -> None:
        self._client = _BaseApiClient(
            api_key,
            smart_rate_limiting,
            timeout,
            max_rate_limit_retries,
            max_server_error_retries,
        )

        self.account = AccountEndpoint(self._client)
        self.champion_mastery = ChampionMasteryEndpoint(self._client)
        self.champion = ChampionEndpoint(self._client)
        self.clash = ClashEndpoint(self._client)
        self.league_exp = LeagueExpEndpoint(self._client)
        self.league = LeagueEndpoint(self._client)
        self.lol_challenges = ChallengesEndpoint(self._client)
        self.lol_status = StatusEndpoint(self._client)
        self.match = MatchEndpoint(self._client)
        self.spectator = SpectatorEndpoint(self._client)
        self.summoner = SummonerEndpoint(self._client)


class DataDragon:
    def __init__(self, version: str | None = None, timeout: int = 10) -> None:
        self._client = _BaseDataDragonClient(version, timeout)

        self.versions = VersionsData(self._client)
        self.champions = ChampionsData(self._client)
        self.challenges = ChallengesData(self._client)
