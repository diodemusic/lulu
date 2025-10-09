from ..base_client import BaseApiClient


class LolChallengesEndpoint:
    def __init__(self, api_key: str | None):
        self.client = BaseApiClient(api_key)
