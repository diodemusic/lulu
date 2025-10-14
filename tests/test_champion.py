from pyke import Pyke, Region
from pyke._models.champion_v3 import ChampionInfo

from .base import api


def test_rotations(api: Pyke):
    rotations = api.champion.rotations(region=Region.EUW)

    assert isinstance(rotations, ChampionInfo)
