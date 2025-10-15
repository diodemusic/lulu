from .._base_client import _BaseApiClient


class TournamentEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client
