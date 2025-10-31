from pyke import Continent, Pyke, Queue, Region
from pyke.models.account_v1 import AccountDto

from .base import api


def test_americas(api: Pyke):
    league = api.league.challenger_leagues_by_queue(Region.NA, Queue.SOLO_DUO)
    puuid = league.entries[0].puuid
    account = api.account.by_puuid(Continent.AMERICAS, puuid)

    assert isinstance(account, AccountDto)


def test_asia(api: Pyke):
    league = api.league.challenger_leagues_by_queue(Region.KR, Queue.SOLO_DUO)
    puuid = league.entries[0].puuid
    account = api.account.by_puuid(Continent.ASIA, puuid)

    assert isinstance(account, AccountDto)


def test_europe(api: Pyke):
    league = api.league.challenger_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)
    puuid = league.entries[0].puuid
    account = api.account.by_puuid(Continent.EUROPE, puuid)

    assert isinstance(account, AccountDto)


def test_sea(api: Pyke):
    league = api.league.challenger_leagues_by_queue(Region.OCE, Queue.SOLO_DUO)
    puuid = league.entries[0].puuid
    account = api.account.by_puuid(Continent.ASIA, puuid)
    match_ids = api.match.match_ids_by_puuid(Continent.SEA, puuid)

    assert isinstance(account, AccountDto)
    assert type(match_ids) is list
    assert match_ids is not None
    assert type(match_ids[0]) is str
