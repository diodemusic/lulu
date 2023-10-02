import lulu

from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_by_puuid():
    clash_data = lulu.clash.clash()

    assert clash_data == "This is some clash data"
