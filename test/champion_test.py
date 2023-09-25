import lulu.src.lulu as lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw


def test_by_puuid():
    champion_rotations = lulu.champion_free_rotation(key, region)

    assert type(champion_rotations.free_champion_ids) == list
    assert type(champion_rotations.free_champion_ids_for_new_players) == list
    assert type(champion_rotations.max_new_player_level) == int
