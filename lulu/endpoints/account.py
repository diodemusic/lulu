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
            continent (Continent): Region to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.

        Returns:
            Account: Instance of the models.account.Account model.
        """

        path = f"/riot/account/v1/accounts/by-puuid/{puuid}"
        data = self.client.continent_request(continent, path)

        return Account(**data)
