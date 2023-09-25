import lulu.src.lulu as lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw


def test_platform():
    platform_status = lulu.status(key, region)

    assert platform_status.platform_id == region.value.upper()
    assert type(platform_status.incidents) == list
    assert type(platform_status.locales) == list
    assert type(platform_status.maintenances) == list
    assert type(platform_status.name) == str
