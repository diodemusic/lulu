from lulu import Division, Lulu, Queue, Region, Tier
from lulu.models.league import LeagueEntry

from .base import api  # type: ignore  # noqa: F401


def test_champion_rotation(api: Lulu):  # noqa: F811
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
