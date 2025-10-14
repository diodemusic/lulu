import os

import pytest
from dotenv import load_dotenv

from pyke import Pyke

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
TEST_PUUID = os.getenv("TEST_PUUID")
TEST_LEAGUE_ID = os.getenv("TEST_LEAGUE_ID")
TEST_CHALLENGE_ID_STR = os.getenv("TEST_CHALLENGE_ID")
if TEST_CHALLENGE_ID_STR:
    TEST_CHALLENGE_ID = int(TEST_CHALLENGE_ID_STR)
TEST_MATCH_ID = os.getenv("TEST_MATCH_ID")


@pytest.fixture
def api() -> Pyke:
    api = Pyke(API_KEY)

    return api
