import lulu
from lulu.models.champion_mastery import ChampionMastery

from .base import TEST_PUUID, api  # type: ignore  # noqa: F401

if not TEST_PUUID:
    quit()


def test_champion_mastery_masteries_by_puuid(api: lulu.Lulu):  # noqa: F811
    champion_masteries = api.champion_mastery.masteries_by_puuid(
        region=lulu.Region.EUW,
        puuid=TEST_PUUID,
    )

    for champion_mastery in champion_masteries:
        assert isinstance(champion_mastery, ChampionMastery)
