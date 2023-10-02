import lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_by_puuid():
    champion_rotations = lulu.champion.free_rotation(region)

    assert type(champion_rotations.free_champion_ids) == list
    assert type(champion_rotations.free_champion_ids_for_new_players) == list
    assert type(champion_rotations.max_new_player_level) == int
