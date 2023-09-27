import lulu.src.lulu as lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw
puuid = "H2qa4P52mGxy6ZRPoqBUaZBZ-Au6GpMSQcgUPc21Qui1TtecAV5mfqPuyLYz9mcDXyoGY4KeuQsiGg"
summoner_id = "Iv6Gdo8TByJF1ymR4XhTUXJ6vIfc3Zk9bEiGu3LIinj6zw1U"
champion_id = 29


def test_by_puuid():
    by_puuid = lulu.mastery_by_puuid(key, region, puuid)

    assert type(by_puuid) == list

    for entry in by_puuid:
        assert entry.puuid == puuid
        assert type(entry.champion_id) == int
        assert type(entry.level) == int
        assert type(entry.points) == int
        assert type(entry.last_play_time) == int
        assert type(entry.points_since_last_level) == int
        assert type(entry.points_until_next_level) == int
        assert type(entry.chest_granted) == bool
        assert type(entry.tokens_earned) == int
        assert entry.summoner_id == summoner_id


def test_by_puuid_and_champion_id():
    by_puuid_and_champion_id = lulu.mastery_by_puuid_and_champion_id(
        key, region, puuid, champion_id
    )

    assert by_puuid_and_champion_id.puuid == puuid
    assert by_puuid_and_champion_id.champion_id == champion_id
    assert type(by_puuid_and_champion_id.level) == int
    assert type(by_puuid_and_champion_id.points) == int
    assert type(by_puuid_and_champion_id.last_play_time) == int
    assert type(by_puuid_and_champion_id.points_since_last_level) == int
    assert type(by_puuid_and_champion_id.points_until_next_level) == int
    assert type(by_puuid_and_champion_id.chest_granted) == bool
    assert type(by_puuid_and_champion_id.tokens_earned) == int
    assert by_puuid_and_champion_id.summoner_id == summoner_id


def test_by_puuid_top():
    by_puuid_top = lulu.mastery_by_puuid_top(key, region, puuid, champion_id)

    assert type(by_puuid_top) == list

    for entry in by_puuid_top:
        assert entry.puuid == puuid
        assert type(entry.champion_id) == int
        assert type(entry.level) == int
        assert type(entry.points) == int
        assert type(entry.last_play_time) == int
        assert type(entry.points_since_last_level) == int
        assert type(entry.points_until_next_level) == int
        assert type(entry.chest_granted) == bool
        assert type(entry.tokens_earned) == int
        assert entry.summoner_id == summoner_id


def test_by_summoner_id():
    by_summoner_id = lulu.mastery_by_summoner_id(key, region, summoner_id)

    assert type(by_summoner_id) == list

    for entry in by_summoner_id:
        assert type(entry.puuid) == str
        assert type(entry.champion_id) == int
        assert type(entry.level) == int
        assert type(entry.points) == int
        assert type(entry.last_play_time) == int
        assert type(entry.points_since_last_level) == int
        assert type(entry.points_until_next_level) == int
        assert type(entry.chest_granted) == bool
        assert type(entry.tokens_earned) == int
        assert entry.summoner_id == summoner_id


def test_by_puuid_and_champion_id():
    by_summoner_id_and_champion_id = lulu.mastery_by_summoner_id_and_champion_id(
        key, region, summoner_id, champion_id
    )

    assert by_summoner_id_and_champion_id.puuid == puuid
    assert by_summoner_id_and_champion_id.champion_id == champion_id
    assert type(by_summoner_id_and_champion_id.level) == int
    assert type(by_summoner_id_and_champion_id.points) == int
    assert type(by_summoner_id_and_champion_id.last_play_time) == int
    assert type(by_summoner_id_and_champion_id.points_since_last_level) == int
    assert type(by_summoner_id_and_champion_id.points_until_next_level) == int
    assert type(by_summoner_id_and_champion_id.chest_granted) == bool
    assert type(by_summoner_id_and_champion_id.tokens_earned) == int
    assert by_summoner_id_and_champion_id.summoner_id == summoner_id


def test_by_summoner_id_top():
    by_summoner_id_top = lulu.mastery_by_summoner_id_top(
        key, region, summoner_id, champion_id
    )

    assert type(by_summoner_id_top) == list

    for entry in by_summoner_id_top:
        assert entry.puuid == puuid
        assert type(entry.champion_id) == int
        assert type(entry.level) == int
        assert type(entry.points) == int
        assert type(entry.last_play_time) == int
        assert type(entry.points_since_last_level) == int
        assert type(entry.points_until_next_level) == int
        assert type(entry.chest_granted) == bool
        assert type(entry.tokens_earned) == int
        assert entry.summoner_id == summoner_id


def test_levels_sum_by_puuid():
    levels_sum_by_puuid = lulu.mastery_levels_sum_by_puuid(key, region, puuid)

    assert type(levels_sum_by_puuid) == int


def test_levels_sum_by_summoner_id():
    levels_sum_by_summoner_id = lulu.mastery_levels_sum_by_summoner_id(
        key, region, summoner_id
    )

    assert type(levels_sum_by_summoner_id) == int
