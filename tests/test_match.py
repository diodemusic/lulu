from pyke import Pyke, Continent
from pyke._models.match_v5 import MatchDto

from .base import TEST_PUUID, api

if not TEST_PUUID:
    quit()


def test_match_ids_by_puuid(api: Pyke):
    match_ids_by_puuid = api.match.match_ids_by_puuid(
        continent=Continent.EUROPE,
        puuid=TEST_PUUID,
        start_time=1744502400,
        end_time=1760313600,
        queue=420,
        type="ranked",
        start=17,
        count=38,
    )

    for match_id in match_ids_by_puuid:
        assert type(match_id) is str
        assert "_" in match_id


def test_by_match_id(api: Pyke):
    by_match_id = api.match.by_match_id(
        continent=Continent.EUROPE, match_id=TEST_MATCH_ID
    )

    assert isinstance(by_match_id, MatchDto)
