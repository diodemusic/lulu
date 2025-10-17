from pyke import Division, Pyke, Queue, Region, Tier
from pyke.models.league_v4 import LeagueEntryDTO, LeagueItemDTO, LeagueListDTO

from .base import TEST_LEAGUE_ID, TEST_PUUID, api

if not TEST_PUUID:
    quit()

if not TEST_LEAGUE_ID:
    quit()


def test_challenger_leagues_by_queue(api: Pyke):
    challenger_leagues_by_queue = api.league.challenger_leagues_by_queue(
        region=Region.EUW, queue=Queue.SOLO_DUO
    )

    assert isinstance(challenger_leagues_by_queue, LeagueListDTO)

    for league_entry in challenger_leagues_by_queue.entries:
        assert isinstance(league_entry, LeagueItemDTO)


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


def test_grandmaster_leagues_by_queue(api: Pyke):
    grandmaster_leagues_by_queue = api.league.grandmaster_leagues_by_queue(
        region=Region.EUW, queue=Queue.SOLO_DUO
    )

    assert isinstance(grandmaster_leagues_by_queue, LeagueListDTO)

    for league_entry in grandmaster_leagues_by_queue.entries:
        assert isinstance(league_entry, LeagueItemDTO)


def test_by_league_id(api: Pyke):
    by_league_id = api.league.by_league_id(region=Region.EUW, league_id=TEST_LEAGUE_ID)

    assert isinstance(by_league_id, LeagueListDTO)

    for league_entry in by_league_id.entries:
        assert isinstance(league_entry, LeagueItemDTO)


def test_master_leagues_by_queue(api: Pyke):
    master_leagues_by_queue = api.league.master_leagues_by_queue(
        region=Region.EUW, queue=Queue.SOLO_DUO
    )

    assert isinstance(master_leagues_by_queue, LeagueListDTO)

    for league_entry in master_leagues_by_queue.entries:
        assert isinstance(league_entry, LeagueItemDTO)
