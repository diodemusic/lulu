from ..base_client import BaseApiClient


class MatchEndpoint:
    def __init__(self, api_key: str | None):
        self.client = BaseApiClient(api_key)
