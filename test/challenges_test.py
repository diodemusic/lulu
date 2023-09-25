import lulu.src.lulu as lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw


def test_config():
    challenges = lulu.challenges_config(key, region)

    assert type(challenges) == list

    for entry in challenges:
        assert type(entry.challenge_id) == int
        assert type(entry.leaderboard) == bool
        assert type(entry.localized_names) == dict
        assert type(entry.state) == str
        assert type(entry.thresholds) == dict


def test_percentiles():
    percentiles = lulu.challenges_percentiles(key, region)

    assert type(percentiles) == dict


def test_apex_players():
    players = lulu.challenges_apex_players(key, region, 0, lulu.level.master)

    assert type(players) == list

    for entry in players:
        assert type(entry.position) == int
        assert type(entry.puuid) == str
        assert type(entry.value) == int


def test_by_puuid():
    player = lulu.challenges(
        key,
        region,
        "H2qa4P52mGxy6ZRPoqBUaZBZ-Au6GpMSQcgUPc21Qui1TtecAV5mfqPuyLYz9mcDXyoGY4KeuQsiGg",
    )

    assert type(player.category_points) == dict
    assert type(player.challenges) == list
    assert type(player.preferences) == dict
    assert type(player.total_points) == dict
