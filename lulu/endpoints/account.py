from ..models.account import Account
from ..enums.continent import Continent


def by_puuid(continent: Continent, puuid: str) -> Account:
    data = {"game_name": "saves", "tag_line": "000", "puuid": puuid}

    account = Account(**data)

    return account
