from .endpoints.account import AccountEndpoint


class Lulu:
    def __init__(self, api_key: str | None):
        self.account = AccountEndpoint(api_key)
