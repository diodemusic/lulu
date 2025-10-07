import os

import pytest
from dotenv import load_dotenv

import lulu

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")


@pytest.fixture
def api() -> lulu.Lulu:
    api = lulu.Lulu(API_KEY)

    return api
