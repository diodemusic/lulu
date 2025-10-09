from ..base_client import BaseApiClient
from ..enums.continent import Continent
from ..enums.region import Region
from ..models.account import Account, AccountRegion


class AccountEndpoint:
    def __init__(self, api_key: str | None):
        self.client = BaseApiClient(api_key)

    def by_puuid(self, continent: Continent, puuid: str) -> Account:
        """Get account by puuid.

        Args:
            continent (Continent): Continent to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.

        Returns:
            Account: lulu.models.account.Account object.
        """

        path = f"/riot/account/v1/accounts/by-puuid/{puuid}"
        data = self.client.continent_request(continent=continent, path=path)

        return Account(**data)

    def by_riot_id(
        self, continent: Continent, game_name: str, tag_line: str
    ) -> Account:
        """Get account by riot id.

        Args:
            continent (Continent): Continent to execute against.
            game_name (str): Riot id game name.
            tag_line (str): Riot id tag line.

        Returns:
            Account: lulu.models.account.Account object.
        """

        path = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        data = self.client.continent_request(continent=continent, path=path)

        return Account(**data)

    def region_by_puuid(self, continent: Continent, puuid: str) -> AccountRegion:
        """Get active region (lol and tft)

        Args:
            continent (Continent): Continent to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.

        Returns:
            AccountRegion: lulu.models.account.AccountRegion object.
        """

        path = f"/riot/account/v1/region/by-game/lol/by-puuid/{puuid}"
        data = self.client.continent_request(continent=continent, path=path)
        data["region"] = Region(data["region"])

        return AccountRegion(**data)
