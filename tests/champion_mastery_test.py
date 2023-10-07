import lulu
from dotenv import load_dotenv
import os
import utils


load_dotenv()
key = os.getenv("KEY")
puuid = os.getenv("PUUID")
summoner_id = os.getenv("SUMMONER_ID")
region = lulu.region.euw
champion_id = 29


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_by_puuid():
    instances = lulu.champion_mastery.by_puuid(region, puuid)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.ChampionMastery
        assert type(instance.puuid) == str
        assert type(instance.champion_id) == int
        assert type(instance.champion_level) == int
        assert type(instance.champion_points) == int
        assert type(instance.last_play_time) == int
        assert type(instance.champion_points_since_last_level) == int
        assert type(instance.champion_points_until_next_level) == int
        assert type(instance.chest_granted) == bool
        assert type(instance.tokens_earned) == int
        assert type(instance.summoner_id) == str


def test_by_puuid_and_champion():
    instance = lulu.champion_mastery.by_puuid_and_champion(region, puuid, champion_id)

    assert type(instance) == utils.classes.ChampionMastery
    assert type(instance.puuid) == str
    assert type(instance.champion_id) == int
    assert type(instance.champion_level) == int
    assert type(instance.champion_points) == int
    assert type(instance.last_play_time) == int
    assert type(instance.champion_points_since_last_level) == int
    assert type(instance.champion_points_until_next_level) == int
    assert type(instance.chest_granted) == bool
    assert type(instance.tokens_earned) == int
    assert type(instance.summoner_id) == str


def test_by_puuid_top():
    instances = lulu.champion_mastery.by_puuid_top(region, puuid, champion_id)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.ChampionMastery
        assert type(instance.puuid) == str
        assert type(instance.champion_id) == int
        assert type(instance.champion_level) == int
        assert type(instance.champion_points) == int
        assert type(instance.last_play_time) == int
        assert type(instance.champion_points_since_last_level) == int
        assert type(instance.champion_points_until_next_level) == int
        assert type(instance.chest_granted) == bool
        assert type(instance.tokens_earned) == int
        assert type(instance.summoner_id) == str


def test_by_summoner():
    instances = lulu.champion_mastery.by_summoner(region, summoner_id)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.ChampionMastery
        assert type(instance.puuid) == str
        assert type(instance.champion_id) == int
        assert type(instance.champion_level) == int
        assert type(instance.champion_points) == int
        assert type(instance.last_play_time) == int
        assert type(instance.champion_points_since_last_level) == int
        assert type(instance.champion_points_until_next_level) == int
        assert type(instance.chest_granted) == bool
        assert type(instance.tokens_earned) == int
        assert type(instance.summoner_id) == str


def test_by_summoner_and_champion():
    instance = lulu.champion_mastery.by_summoner_and_champion(
        region, summoner_id, champion_id
    )

    assert type(instance) == utils.classes.ChampionMastery
    assert type(instance.puuid) == str
    assert type(instance.champion_id) == int
    assert type(instance.champion_level) == int
    assert type(instance.champion_points) == int
    assert type(instance.last_play_time) == int
    assert type(instance.champion_points_since_last_level) == int
    assert type(instance.champion_points_until_next_level) == int
    assert type(instance.chest_granted) == bool
    assert type(instance.tokens_earned) == int
    assert type(instance.summoner_id) == str


def test_by_summoner_top():
    instances = lulu.champion_mastery.by_summoner_top(region, summoner_id, champion_id)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.ChampionMastery
        assert type(instance.puuid) == str
        assert type(instance.champion_id) == int
        assert type(instance.champion_level) == int
        assert type(instance.champion_points) == int
        assert type(instance.last_play_time) == int
        assert type(instance.champion_points_since_last_level) == int
        assert type(instance.champion_points_until_next_level) == int
        assert type(instance.chest_granted) == bool
        assert type(instance.tokens_earned) == int
        assert type(instance.summoner_id) == str


def test_scores_by_puuid():
    instance = lulu.champion_mastery.scores_by_puuid(region, puuid)

    assert type(instance) == int


def test_scores_by_summoner():
    instance = lulu.champion_mastery.scores_by_summoner(region, summoner_id)

    assert type(instance) == int
