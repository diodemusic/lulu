import pytest

from pyke import DataDragon

TEST_REGION = "en_GB"


@pytest.fixture
def ddragon() -> DataDragon:
    ddragon = DataDragon()

    return ddragon
