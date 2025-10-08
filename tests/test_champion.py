import lulu
from lulu.models.champion import ChampionInfo

from .base import api  # type: ignore  # noqa: F401


def test_champion_rotation(api: lulu.Lulu):  # noqa: F811
    champion_rotation = api.champion.rotations(lulu.Region.EUW)

    print(champion_rotation)

    assert isinstance(champion_rotation, ChampionInfo)
