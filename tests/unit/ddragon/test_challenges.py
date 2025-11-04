from pyke import DataDragon

from .base import ddragon


def test_get_all(ddragon: DataDragon):
    get_all = ddragon.challenges.get_all("en_GB")

    assert isinstance(get_all, list)

    for challenge in get_all:
        assert isinstance(challenge, dict)
