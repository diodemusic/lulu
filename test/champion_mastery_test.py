import lulu.src.lulu as lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw


def test_by_puuid():
    puuid = (
        "H2qa4P52mGxy6ZRPoqBUaZBZ-Au6GpMSQcgUPc21Qui1TtecAV5mfqPuyLYz9mcDXyoGY4KeuQsiGg"
    )
    by_puuid = lulu.mastery_by_puuid(key, region, puuid)

    assert type(by_puuid) == list

    for entry in by_puuid:
        assert entry.puuid == puuid
        assert type(entry.champion_id) == int
        assert type(entry.level) == int
        assert type(entry.points) == int
        assert type(entry.last_play_time) == int
        assert type(entry.points_since_last_level) == int
        assert type(entry.points_until_next_level) == int
        assert type(entry.chest_granted) == bool
        assert type(entry.tokens_earned) == int
        assert type(entry.summoner_id) == str


def test_by_summoner_id():
    summoner_id = "Iv6Gdo8TByJF1ymR4XhTUXJ6vIfc3Zk9bEiGu3LIinj6zw1U"
    by_summoner_id = lulu.mastery_by_summoner_id(key, region, summoner_id)

    assert type(by_summoner_id) == list

    for entry in by_summoner_id:
        assert type(entry.puuid) == str
        assert type(entry.champion_id) == int
        assert type(entry.level) == int
        assert type(entry.points) == int
        assert type(entry.last_play_time) == int
        assert type(entry.points_since_last_level) == int
        assert type(entry.points_until_next_level) == int
        assert type(entry.chest_granted) == bool
        assert type(entry.tokens_earned) == int
        assert type(entry.summoner_id) == str
