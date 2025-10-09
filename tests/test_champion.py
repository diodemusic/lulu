from lulu import Lulu, Region
from lulu.models.champion import ChampionInfo

from .base import api  # type: ignore  # noqa: F401


def test_champion_rotation(api: Lulu):  # noqa: F811
    champion_rotation = api.champion.rotations(Region.EUW)

    print(champion_rotation)

    assert isinstance(champion_rotation, ChampionInfo)
