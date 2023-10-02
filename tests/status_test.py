import lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_platform():
    platform_status = lulu.status.by_region(region)

    assert platform_status.platform_id == region.upper()
    assert type(platform_status.incidents) == list
    assert type(platform_status.locales) == list
    assert type(platform_status.maintenances) == list
    assert type(platform_status.name) == str
