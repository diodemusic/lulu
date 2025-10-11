from pyke import Pyke, Region
from pyke._models.champion_mastery_v4 import ChampionMasteryDto

from .base import TEST_PUUID, api

if not TEST_PUUID:
    quit()


def test_champion_mastery_masteries_by_puuid(api: Pyke):
    champion_mastery_masteries_by_puuid = api.champion_mastery.masteries_by_puuid(
        region=Region.EUW,
        puuid=TEST_PUUID,
    )

    for champion_mastery in champion_mastery_masteries_by_puuid:
        assert isinstance(champion_mastery, ChampionMasteryDto)


def test_champion_mastery_by_puuid_and_champion_id(api: Pyke):
    champion_mastery_by_puuid_and_champion_id = (
        api.champion_mastery.by_puuid_and_champion_id(
            region=Region.EUW, puuid=TEST_PUUID, champion_id=11
        )
    )

    assert isinstance(champion_mastery_by_puuid_and_champion_id, ChampionMasteryDto)


def test_champion_mastery_masteries_by_puuid_top(api: Pyke):
    champion_mastery_masteries_by_puuid_top = (
        api.champion_mastery.masteries_by_puuid_top(
            region=Region.EUW, puuid=TEST_PUUID, count=10
        )
    )

    assert len(champion_mastery_masteries_by_puuid_top) == 10

    for champion_mastery in champion_mastery_masteries_by_puuid_top:
        assert isinstance(champion_mastery, ChampionMasteryDto)

    champion_mastery_masteries_by_puuid_top = (
        api.champion_mastery.masteries_by_puuid_top(region=Region.EUW, puuid=TEST_PUUID)
    )

    assert len(champion_mastery_masteries_by_puuid_top) == 3

    for champion_mastery in champion_mastery_masteries_by_puuid_top:
        assert isinstance(champion_mastery, ChampionMasteryDto)


def test_champion_mastery_score_by_puuid(api: Pyke):
    champion_mastery_score_by_puuid = api.champion_mastery.score_by_puuid(
        region=Region.EUW, puuid=TEST_PUUID
    )

    assert isinstance(champion_mastery_score_by_puuid, int)
