from lulu import continent, match
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
puuid = os.getenv("PUUID")
continent = continent.europe
queue = 400
match_id = match.history(key, continent, puuid, queue, 1)[0]


def test_history():
    count = 10
    start = 3
    history = match.history(key, continent, puuid, queue, start, count)

    assert type(history) == list
    assert len(history) == count


def test_by_match_id():
    match_data = match.by_match_id(key, continent, match_id)
    info = match_data.info
    metadata = match_data.metadata

    assert type(info.creation) == int
    assert type(info.duration) == int
    assert type(info.end_timestamp) == int
    assert type(info.game_id) == int
    assert type(info.mode) == str
    assert type(info.name) == str
    assert type(info.game_type) == str
    assert type(info.version) == str
    assert type(info.map_id) == int
    assert type(info.participants) == list

    for participant in info.participants:
        assert type(participant) == dict

    assert type(info.platform_id) == str
    assert info.queue_id == queue
    assert type(info.teams) == list

    for team in info.teams:
        assert type(team) == dict

    assert type(info.tournament_code) == str

    assert type(metadata.data_version) == str
    assert metadata.match_id == match_id
    assert type(metadata.participants) == list


def test_timeline_by_match_id():
    timeline_by_match_id = match.timeline_by_match_id(key, continent, match_id)

    info = timeline_by_match_id.info
    metadata = timeline_by_match_id.metadata

    assert type(info.frame_interval) == int
    assert type(info.frames) == list

    for frame in info.frames:
        assert type(frame) == dict

    assert type(info.game_id) == int
    assert type(info.participants) == list

    for participant in info.participants:
        assert type(participant) == dict

    assert type(metadata.data_version) == str
    assert metadata.match_id == match_id
    assert type(metadata.participants) == list
