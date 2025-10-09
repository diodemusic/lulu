from pyke import Division, Pyke, Queue, Region, Tier
from pyke.models.league import LeagueEntry

from .base import api  # type: ignore  # noqa: F401


def test_champion_rotation(api: Pyke):  # noqa: F811
    league_entries = api.league_exp.entries_by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
    )

    for league_entry in league_entries:
        assert isinstance(league_entry, LeagueEntry)

    league_entries = api.league_exp.entries_by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
    )

    for league_entry in league_entries:
        assert isinstance(league_entry, LeagueEntry)
