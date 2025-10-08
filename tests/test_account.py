import lulu
from lulu.models.account import Account, AccountRegion

from .base import TEST_PUUID, api  # type: ignore  # noqa: F401

if not TEST_PUUID:
    quit()


def test_account_by_puuid(api: lulu.Lulu):  # noqa: F811
    account_by_puuid = api.account.by_puuid(
        continent=lulu.Continent.EUROPE,
        puuid=TEST_PUUID,
    )

    assert isinstance(account_by_puuid, Account)


def test_account_by_riot_id(api: lulu.Lulu):  # noqa: F811
    account_by_riot_id = api.account.by_riot_id(
        continent=lulu.Continent.EUROPE, game_name="saves", tag_line="000"
    )

    assert isinstance(account_by_riot_id, Account)


def test_account_region_by_puuid(api: lulu.Lulu):  # noqa: F811
    account_region_by_puuid = api.account.region_by_puuid(
        continent=lulu.Continent.EUROPE, puuid=TEST_PUUID
    )

    assert isinstance(account_region_by_puuid, AccountRegion)
