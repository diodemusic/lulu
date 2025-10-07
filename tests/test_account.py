from .base import lu  # type: ignore  # noqa: F401
from lulu.enums.continent import Continent
from lulu import Lulu


def test_account(lu: Lulu):  # noqa: F811
    # Returns AccountDTO {puuid: str, gameName: str?, tagLine: str?}
    account = lu.account_by_puuid(continent=Continent.EUROPE, puuid="123")

    # assert type(account) == Account
    assert account.game_name == "saves"
    assert account.tag_line == "000"
    assert account.puuid == "123"
