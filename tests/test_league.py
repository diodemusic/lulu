from pyke import Pyke, Queue, Region
from pyke._models.league_v4 import LeagueListDTO

from .base import api  # type: ignore  # noqa: F401


def test_challenger_leagues_by_queue(api: Pyke):  # noqa: F811
    challenger_leagues_by_queue = api.league.challenger_leagues_by_queue(
        Region.EUW, Queue.SOLO_DUO
    )

    assert isinstance(challenger_leagues_by_queue, LeagueListDTO)
