from .._base_client import _BaseApiClient


class RsoMatchEndpoint:
    def __init__(self, api_key: str | None):
        self._client = _BaseApiClient(api_key)
