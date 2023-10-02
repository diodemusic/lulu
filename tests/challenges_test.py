import lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw
puuid = os.getenv("PUUID")
challenge_id = 0
level = lulu.level.master


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_config():
    challenges_config = lulu.challenges.config(region)

    assert type(challenges_config) == list

    for entry in challenges_config:
        assert type(entry.challenge_id) == int
        assert type(entry.leaderboard) == bool
        assert type(entry.localized_names) == dict
        assert type(entry.state) == str
        assert type(entry.thresholds) == dict


def test_percentiles():
    percentiles = lulu.challenges.percentiles(region)

    assert type(percentiles) == dict


def test_config_by_challenge_id():
    challenges_config_by_challenge_id = lulu.challenges.config_by_challenge_id(
        region, challenge_id
    )

    assert challenges_config_by_challenge_id.challenge_id == 0
    assert type(challenges_config_by_challenge_id.leaderboard) == bool
    assert type(challenges_config_by_challenge_id.localized_names) == dict
    assert type(challenges_config_by_challenge_id.state) == str
    assert type(challenges_config_by_challenge_id.thresholds) == dict


def test_apex_players():
    apex_players = lulu.challenges.apex_players(region, challenge_id, level)

    assert type(apex_players) == list

    for entry in apex_players:
        assert type(entry.position) == int
        assert type(entry.puuid) == str
        assert type(entry.value) == int


def test_percentiles_by_challenge_id():
    percentiles_by_challenge_id = lulu.challenges.percentiles_by_challenge_id(
        region, challenge_id
    )

    assert type(percentiles_by_challenge_id.iron) == float
    assert type(percentiles_by_challenge_id.bronze) == float
    assert type(percentiles_by_challenge_id.silver) == float
    assert type(percentiles_by_challenge_id.gold) == float
    assert type(percentiles_by_challenge_id.platinum) == float
    assert type(percentiles_by_challenge_id.diamond) == float
    assert type(percentiles_by_challenge_id.master) == float
    assert type(percentiles_by_challenge_id.grandmaster) == float
    assert type(percentiles_by_challenge_id.challenger) == float
    assert type(percentiles_by_challenge_id.none) == float


def test_by_puuid():
    player = lulu.challenges.by_puuid(
        region,
        puuid,
    )

    assert type(player.category_points) == dict
    assert type(player.challenges) == list
    assert type(player.preferences) == dict
    assert type(player.total_points) == dict
