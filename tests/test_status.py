from pyke import Pyke, Region
from pyke._models.status_v4 import PlatformDataDto

from .base import api


def test_platform_data(api: Pyke):
    test_platform_data = api.status.platform_data(region=Region.EUW)

    assert isinstance(test_platform_data, PlatformDataDto)
