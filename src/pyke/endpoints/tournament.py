from .._base_client import _BaseApiClient


class TournamentEndpoint:
    def __init__(self, api_key: str | None):
        self._client = _BaseApiClient(api_key)
