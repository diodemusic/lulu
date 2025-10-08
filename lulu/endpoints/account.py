from ..base_client import BaseApiClient
from ..enums.continent import Continent
from ..models.account import Account


class AccountEndpoint:
    def __init__(self, api_key: str | None):
        self.client = BaseApiClient(api_key)

    def by_puuid(self, continent: Continent, puuid: str) -> Account:
        """
        Get account by puuid.

        Args:
            continent (Continent): Continent to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.

        Returns:
            Account: Instance of the lulu.models.account.Account model.
        """

        path = f"/riot/account/v1/accounts/by-puuid/{puuid}"
        data = self.client.continent_request(continent=continent, path=path)

        return Account(**data)

    def by_riot_id(
        self, continent: Continent, game_name: str, tag_line: str
    ) -> Account:
        """
        Get account by riot id.

        Args:
            continent (Continent): Continent to execute against.
            game_name (str): Riot id game name.
            tag_line (str): Riot id tag line.

        Returns:
            Account: Instance of the lulu.models.account.Account model.
        """
        path = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        data = self.client.continent_request(continent=continent, path=path)

        return Account(**data)
