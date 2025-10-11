from pyke import Division, Pyke, Queue, Region, Tier
from pyke._models.league_v4 import LeagueEntryDTO, LeagueListDTO

from .base import TEST_PUUID, api

if not TEST_PUUID:
    quit()


def test_challenger_leagues_by_queue(api: Pyke):
    challenger_leagues_by_queue = api.league.challenger_leagues_by_queue(
        region=Region.EUW, queue=Queue.SOLO_DUO
    )

    assert isinstance(challenger_leagues_by_queue, LeagueListDTO)


def test_by_puuid(api: Pyke):
    by_puuid = api.league.by_puuid(region=Region.EUW, puuid=TEST_PUUID)

    for league_entry in by_puuid:
        assert isinstance(league_entry, LeagueEntryDTO)


def test_by_queue_tier_division(api: Pyke):
    by_queue_tier_division = api.league.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
    )

    for league_entry in by_queue_tier_division:
        assert isinstance(league_entry, LeagueEntryDTO)

    by_queue_tier_division = api.league.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
    )

    for league_entry in by_queue_tier_division:
        assert isinstance(league_entry, LeagueEntryDTO)
