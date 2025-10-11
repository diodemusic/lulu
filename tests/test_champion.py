from pyke import Pyke, Region
from pyke._models.champion_v3 import ChampionInfo

from .base import api


def test_champion_rotation(api: Pyke):
    champion_rotation = api.champion.rotations(Region.EUW)

    print(champion_rotation)

    assert isinstance(champion_rotation, ChampionInfo)
