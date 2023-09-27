import lulu.src.lulu as lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
continent = lulu.continent.europe
puuid = "H2qa4P52mGxy6ZRPoqBUaZBZ-Au6GpMSQcgUPc21Qui1TtecAV5mfqPuyLYz9mcDXyoGY4KeuQsiGg"


def test_by_puuid():
    by_puuid = lulu.account_by_puuid(key, continent, puuid)

    assert by_puuid.puuid == puuid
    assert by_puuid.game_name == "saves"
    assert by_puuid.tag_line == "000"


def test_by_riot_id():
    by_riot_id = lulu.account_by_riot_id(key, continent, "saves", "000")

    assert by_riot_id.puuid == puuid
    assert by_riot_id.game_name == "saves"
    assert by_riot_id.tag_line == "000"
