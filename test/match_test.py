import lulu.src.lulu as lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
continent = lulu.continent.europe
puuid = "H2qa4P52mGxy6ZRPoqBUaZBZ-Au6GpMSQcgUPc21Qui1TtecAV5mfqPuyLYz9mcDXyoGY4KeuQsiGg"


def test_match_history():
    queue = 420
    count = 10
    start = 3
    history = lulu.match_history(key, continent, puuid, queue, start, count)

    assert type(history) == list
    assert len(history) == count
