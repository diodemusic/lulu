import lulu
from dotenv import load_dotenv
import os
import utils


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_champion_rotations():
    instance = lulu.champion.champion_rotations(region)

    assert type(instance) == utils.classes.ChampionInfo
    assert type(instance.free_champion_ids) == list

    for free_champion_id in instance.free_champion_ids:
        assert type(free_champion_id) == int

    assert type(instance.free_champion_ids_for_new_players) == list

    for free_champion_id_for_new_players in instance.free_champion_ids_for_new_players:
        assert type(free_champion_id_for_new_players) == int

    assert type(instance.max_new_player_level) == int
