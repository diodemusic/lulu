from .endpoints.account import AccountEndpoint


class Lulu:
    """Main entrypoint for interacting with the Riot API."""

    def __init__(self, api_key: str | None):
        self.account = AccountEndpoint(api_key)
