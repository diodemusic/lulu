from .._base_client import _BaseApiClient
from .._models.account_v1 import AccountDto, AccountRegionDTO
from ..enums.continent import Continent
from ..enums.region import Region


class AccountEndpoint:
    def __init__(self, api_key: str | None):
        self._client = _BaseApiClient(api_key)

    def by_puuid(self, continent: Continent, puuid: str) -> AccountDto:
        """Get account by puuid.

        Args:
            continent (Continent): Continent to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.

        Returns:
            AccountDto: pyke.models.account.AccountDto object.
        """

        path = f"/riot/account/v1/accounts/by-puuid/{puuid}"
        data = self._client._continent_request(continent=continent, path=path)

        return AccountDto(**data)

    def by_riot_id(
        self, continent: Continent, game_name: str, tag_line: str
    ) -> AccountDto:
        """Get account by riot id.

        Args:
            continent (Continent): Continent to execute against.
            game_name (str): Riot id game name.
            tag_line (str): Riot id tag line.

        Returns:
            AccountDto: pyke.models.account.AccountDto object.
        """

        path = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        data = self._client._continent_request(continent=continent, path=path)

        return AccountDto(**data)

    def region_by_puuid(self, continent: Continent, puuid: str) -> AccountRegionDTO:
        """Get active region (lol and tft)

        Args:
            continent (Continent): Continent to execute against.
            puuid (str): Encrypted PUUID. Exact length of 78 characters.

        Returns:
            AccountRegionDTO: pyke.models.account.AccountRegionDTO object.
        """

        path = f"/riot/account/v1/region/by-game/lol/by-puuid/{puuid}"
        data = self._client._continent_request(continent=continent, path=path)
        data["region"] = Region(data["region"])

        return AccountRegionDTO(**data)
