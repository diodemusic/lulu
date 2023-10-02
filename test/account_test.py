import lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
puuid = os.getenv("PUUID")
game_name = os.getenv("GAME_NAME")
tag_line = os.getenv("TAG_LINE")
continent = lulu.continent.europe


def test_by_puuid():
    by_puuid = lulu.account.by_puuid(key, continent, puuid)

    assert by_puuid.puuid == puuid
    assert by_puuid.game_name == game_name
    assert by_puuid.tag_line == tag_line


def test_by_riot_id():
    by_riot_id = lulu.account.by_riot_id(key, continent, game_name, tag_line)

    assert by_riot_id.puuid == puuid
    assert by_riot_id.game_name == game_name
    assert by_riot_id.tag_line == tag_line
