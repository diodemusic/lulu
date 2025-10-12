from pyke import Pyke, Region
from pyke._models.challenges_v1 import ChallengeConfigInfoDto

from .base import api


def test_config(api: Pyke):
    config = api.challenges.config(region=Region.EUW)

    for challenge in config:
        assert isinstance(challenge, ChallengeConfigInfoDto)
