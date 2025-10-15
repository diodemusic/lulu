from .._base_client import _BaseApiClient


class StatusEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client
