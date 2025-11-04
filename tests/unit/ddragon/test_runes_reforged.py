from pyke import DataDragon

from .base import ddragon


def test_get_all(ddragon: DataDragon):
    get_all = ddragon.runes_reforged.get_all("en_GB")

    assert isinstance(get_all, list)

    for rune in get_all:
        assert isinstance(rune, dict)
