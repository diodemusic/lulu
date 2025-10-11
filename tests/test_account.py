from pyke import Continent, Pyke
from pyke._models.account_v1 import AccountDto, AccountRegionDTO

from .base import TEST_PUUID, api

if not TEST_PUUID:
    quit()


def test_account_by_puuid(api: Pyke):
    account_by_puuid = api.account.by_puuid(
        continent=Continent.EUROPE,
        puuid=TEST_PUUID,
    )

    assert isinstance(account_by_puuid, AccountDto)


def test_account_by_riot_id(api: Pyke):
    account_by_riot_id = api.account.by_riot_id(
        continent=Continent.EUROPE, game_name="saves", tag_line="000"
    )

    assert isinstance(account_by_riot_id, AccountDto)


def test_account_region_by_puuid(api: Pyke):
    account_region_by_puuid = api.account.region_by_puuid(
        continent=Continent.EUROPE, puuid=TEST_PUUID
    )

    assert isinstance(account_region_by_puuid, AccountRegionDTO)
