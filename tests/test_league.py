from pyke import Pyke, Queue, Region
from pyke._models.league_v4 import LeagueListDTO

from .base import api


def test_challenger_leagues_by_queue(api: Pyke):
    challenger_leagues_by_queue = api.league.challenger_leagues_by_queue(
        Region.EUW, Queue.SOLO_DUO
    )

    assert isinstance(challenger_leagues_by_queue, LeagueListDTO)


def test_by_puuid(api: Pyke):
    pass
