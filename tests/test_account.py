import lulu

from .base import TEST_PUUID, api  # type: ignore  # noqa: F401


def test_account_by_puuid(api: lulu.Lulu):  # noqa: F811
    if not TEST_PUUID:
        quit()

    # Returns AccountDTO {puuid: str, gameName: str?, tagLine: str?}
    account = api.account.by_puuid(
        continent=lulu.Continent.EUROPE,
        puuid=TEST_PUUID,
    )

    # assert type(account) == Account
    assert account.game_name == "saves"
    assert account.tag_line == "000"
    assert account.puuid == TEST_PUUID
