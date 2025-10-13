from pyke import Pyke, Region
from pyke._models.challenges_v1 import ChallengeConfigInfoDto

from .base import api


def test_config(api: Pyke):
    config = api.challenges.config(region=Region.EUW)

    for challenge in config:
        assert isinstance(challenge, ChallengeConfigInfoDto)


def test_percentiles(api: Pyke):
    percentiles = api.challenges.percentiles(region=Region.EUW)

    assert type(percentiles) is dict


def test_config_by_challenge_id(api: Pyke):
    config_by_challenge_id = api.challenges.config_by_challenge_id(
        region=Region.EUW, challenge_id=TEST_CHELLENGE_ID
    )

    assert isinstance(config_by_challenge_id, ChallengeConfigInfoDto)


def test_leaderboards_by_level(api: Pyke):
    leaderboards_by_level = api.challenges.leaderboards_by_level(
        region=Region.EUW, level=Level.PLATINUM, challenge_id=TEST_CHALLENGE_ID
    )
