from lulu import region, spectator
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = region.euw
summoner_id = None  # get from .env spectator game_name + tag_line


def _by_summoner_id():
    by_summoner_id = spectator.by_summoner_id(key, region, summoner_id)

    assert type(by_summoner_id.banned_champions) == list

    for player in by_summoner_id.banned_champions:
        assert type(player) == dict

    assert type(by_summoner_id.length) == int
    assert type(by_summoner_id.mode) == str
    assert type(by_summoner_id.queue_config_id) == int
    assert type(by_summoner_id.start_time) == int
    assert type(by_summoner_id.game_type) == str
    assert type(by_summoner_id.map_id) == int
    assert type(by_summoner_id.observers) == dict
    assert type(by_summoner_id.participants) == list

    for participant in by_summoner_id.participants:
        assert type(participant) == dict

    assert type(by_summoner_id.platform_id) == str


def _featured_games():
    featured_games = spectator.featured_games(key, region)

    assert type(featured_games.client_refresh_interval) == int
    assert type(featured_games.game_list) == list

    for game in featured_games.game_list:
        assert type(game) == dict


def test_temp():
    assert 1 == 1
