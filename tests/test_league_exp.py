from pyke import Division, Pyke, Queue, Region, Tier
from pyke._models.league_exp_v4 import LeagueEntryDTO

from .base import api


def test_entries_by_queue_tier_division(api: Pyke):
    entries_by_queue_tier_division = api.league_exp.entries_by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
    )

    for league_entry in entries_by_queue_tier_division:
        assert isinstance(league_entry, LeagueEntryDTO)

    entries_by_queue_tier_division = api.league_exp.entries_by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
    )

    for league_entry in entries_by_queue_tier_division:
        assert isinstance(league_entry, LeagueEntryDTO)
