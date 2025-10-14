from pyke import Level, Pyke, Region
from pyke._models.challenges_v1 import (
    ApexPlayerInfoDto,
    ChallengeConfigInfoDto,
    PlayerInfoDto,
)

from .base import TEST_CHALLENGE_ID, TEST_PUUID, api

if not TEST_PUUID:
    quit()

if not TEST_CHALLENGE_ID:
    quit()


def test_config(api: Pyke):
    config = api.challenges.config(region=Region.EUW)

    for challenge in config:
        assert isinstance(challenge, ChallengeConfigInfoDto)


def test_percentiles(api: Pyke):
    percentiles = api.challenges.percentiles(region=Region.EUW)

    assert type(percentiles) is dict


def test_config_by_challenge_id(api: Pyke):
    config_by_challenge_id = api.challenges.config_by_challenge_id(
        region=Region.EUW, challenge_id=TEST_CHALLENGE_ID
    )

    assert isinstance(config_by_challenge_id, ChallengeConfigInfoDto)


def test_leaderboards_by_level(api: Pyke):
    leaderboards_by_level = api.challenges.leaderboards_by_level(
        region=Region.EUW, level=Level.MASTER, challenge_id=TEST_CHALLENGE_ID
    )

    for leaderboard in leaderboards_by_level:
        assert isinstance(leaderboard, ApexPlayerInfoDto)


def test_percentiles_by_challenge_id(api: Pyke):
    percentiles_by_challenge_id = api.challenges.percentiles_by_challenge_id(
        region=Region.EUW, challenge_id=TEST_CHALLENGE_ID
    )

    assert type(percentiles_by_challenge_id) is dict


def test_by_puuid(api: Pyke):
    by_puuid = api.challenges.by_puuid(region=Region.EUW, puuid=TEST_PUUID)

    assert isinstance(by_puuid, PlayerInfoDto)
