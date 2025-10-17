from pyke import Division, Pyke, Queue, Region, Tier
from pyke.models.league_exp_v4 import LeagueEntryDTO

from .base import api


def test_by_queue_tier_division(api: Pyke):
    by_queue_tier_division = api.league_exp.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
    )

    for league_entry in by_queue_tier_division:
        assert isinstance(league_entry, LeagueEntryDTO)

    by_queue_tier_division = api.league_exp.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
    )

    for league_entry in by_queue_tier_division:
        assert isinstance(league_entry, LeagueEntryDTO)
