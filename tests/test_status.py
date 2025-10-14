from pyke import Pyke, Region
from pyke._models.status_v4 import PlatformDataDto

from .base import api


def test_platform(api: Pyke):
    platform = api.status.platform(region=Region.EUW)

    assert isinstance(platform, PlatformDataDto)
