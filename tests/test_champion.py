from pyke import Pyke, Region
from pyke.models.champion import ChampionInfo

from .base import api  # type: ignore  # noqa: F401


def test_champion_rotation(api: Pyke):  # noqa: F811
    champion_rotation = api.champion.rotations(Region.EUW)

    print(champion_rotation)

    assert isinstance(champion_rotation, ChampionInfo)
