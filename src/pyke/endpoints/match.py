from pyke import Continent, Type

from .._base_client import _BaseApiClient
from .._models.match_v5 import MatchDto, TimelineDto


class MatchEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def match_ids_by_puuid(
        self,
        continent: Continent,
        puuid: str,
        start_time: int | None = None,
        end_time: int | None = None,
        queue: int | None = None,
        type: Type | None = None,
        start: int | None = None,
        count: int | None = None,
    ) -> list[str]:
        """# Get a list of match ids by puuid

        **Args:**  
            `continent (Continent):` Continent to execute against (pyke._enums.continent.Continent).  
            `puuid (str):` Encrypted PUUID. Exact length of 78 characters.  
            `start_time (int | None, optional):` Epoch timestamp in seconds. The matchlist started storing timestamps on June 16th, 2021. Any matches played before June 16th, 2021 won't be included in the results if the startTime filter is set. Defaults to None.  
            `end_time (int | None, optional):` Epoch timestamp in seconds. Defaults to None.  
            `queue (int | None, optional):` Filter the list of match ids by a specific queue id. This filter is mutually inclusive of the type filter meaning any match ids returned must match both the queue and type filters. Defaults to None.  
            `type (Type | None, optional):` Filter the list of match ids by the type of match. This filter is mutually inclusive of the queue filter meaning any match ids returned must match both the queue and type filters (pyke._enums.type.Type). Defaults to None.  
            `start (int | None, optional):` Start index. Defaults to 0.  
            `count (int | None, optional):` Valid values: 0 to 100. Number of match ids to return. Defaults to 20.  

        **Returns:**  
            `list[str]:` List of match id strings.
        """  # fmt: skip

        path = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "queue": queue,
            "type": type,
            "start": start,
            "count": count,
        }
        data = self._client._continent_request(
            continent=continent, path=path, params=params
        )

        return data

    def by_match_id(self, continent: Continent, match_id: str) -> MatchDto:
        """# Get a match by match id

        **Args:**  
            `continent (Continent):` Continent to execute against (pyke._enums.continent.Continent).  
            `match_id (str):` Match id string.  

        **Returns:**  
            `MatchDto:` pyke._models.match_v5.MatchDto object.
        """  # fmt: skip

        path = f"/lol/match/v5/matches/{match_id}"
        data = self._client._continent_request(continent=continent, path=path)

        return MatchDto(**data)

    def timeline_by_match_id(self, continent: Continent, match_id: str) -> TimelineDto:
        """# Get a match timeline by match id

        **Args:**  
            `continent (Continent):` Continent to execute against (pyke._enums.continent.Continent).  
            `match_id (str):` Match id string.  

        **Returns:**  
            `TimelineDto:` pyke._models.match_v5.TimelineDto object.
        """  # fmt: skip

        path = f"/lol/match/v5/matches/{match_id}/timeline"
        data = self._client._continent_request(continent=continent, path=path)

        return TimelineDto(**data)
