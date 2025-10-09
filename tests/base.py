import os

import pytest
from dotenv import load_dotenv

from lulu import Lulu

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
TEST_PUUID = os.getenv("TEST_PUUID")

if not API_KEY:
    print("Please add RIOT_API_KEY to .env")
    quit()

if not TEST_PUUID:
    print("Please add TEST_PUUID to .env")
    quit()


@pytest.fixture
def api() -> Lulu:
    api = Lulu(API_KEY)

    return api
