from pyke import Queue, Region

from .._base_client import _BaseApiClient
from .._models.league_v4 import LeagueListDTO


class LeagueEndpoint:
    def __init__(self, api_key: str | None):
        self._client = _BaseApiClient(api_key)

    def challenger_leagues_by_queue(
        self,
        region: Region,
        queue: Queue,
    ) -> LeagueListDTO:
        """Get the challenger league for given queue.

        Args:
            region (Region): Region to execute against (pyke.enums.region.Region).
            queue (Queue): Ranked queue type (pyke.enums.queue.Queue).

        Returns:
            LeagueListDTO: pyke.models.league_v4.LeagueListDTO object.
        """

        path = f"/lol/league/v4/challengerleagues/by-queue/{queue.value}"
        data = self._client._region_request(region=region, path=path)

        return LeagueListDTO(**data)
