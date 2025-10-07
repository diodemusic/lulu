from .endpoints import account
from .models.account import Account
from .enums.continent import Continent


class Lulu:
    def __init__(self, api_key: str):
        self._api_key = api_key

    def account_by_puuid(self, continent: Continent, puuid: str) -> Account:
        data = account.by_puuid(continent=continent, puuid=puuid)

        return data
