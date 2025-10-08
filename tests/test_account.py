import lulu
from lulu.models.account import Account

from .base import TEST_PUUID, api  # type: ignore  # noqa: F401


def test_account_by_puuid(api: lulu.Lulu):  # noqa: F811
    if not TEST_PUUID:
        quit()

    account = api.account.by_puuid(
        continent=lulu.Continent.EUROPE,
        puuid=TEST_PUUID,
    )

    assert type(account) is Account
    assert account.game_name == "saves"
    assert account.tag_line == "000"
    assert account.puuid == TEST_PUUID


def test_account_by_riot_id(api: lulu.Lulu):  # noqa: F811
    if not TEST_PUUID:
        quit()

    account = api.account.by_riot_id(
        continent=lulu.Continent.EUROPE, game_name="saves", tag_line="000"
    )

    assert type(account) is Account
    assert account.game_name == "saves"
    assert account.tag_line == "000"
    assert account.puuid == TEST_PUUID
