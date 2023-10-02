from lulu import region, status
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = region.euw


def test_platform():
    platform_status = status.by_region(key, region)

    assert platform_status.platform_id == region.upper()
    assert type(platform_status.incidents) == list
    assert type(platform_status.locales) == list
    assert type(platform_status.maintenances) == list
    assert type(platform_status.name) == str
