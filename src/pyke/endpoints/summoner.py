from .._base_client import _BaseApiClient


class SummonerEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client
