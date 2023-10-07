class SettingsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._instance.api_key = "RIOT_API_KEY"
            cls._instance.cache_ttl = 3600
            cls._instance.cache_enabled = True
        return cls._instance

    def set_api_key(self, api_key: str) -> None:
        """Set the Riot API key.

        Args:
            api_key (str): Riot API key.
        """

        self.api_key = api_key

    def set_cache_ttl(self, cache_ttl: int) -> None:
        """Set the cache TTL (in seconds).

        Args:
            cache_ttl (int): The new cache TTL.
        """

        self.cache_ttl = cache_ttl

    def set_cache_enabled(self, cache_enabled: bool) -> None:
        """Set the cache enabled.

        Args:
            cache_ttl (bool): The new cache enabled.
        """

        self.cache_enabled = cache_enabled

    def get_api_key(self) -> str:
        """Get the current Riot API key.

        Returns:
            str: The current Riot API key.
        """

        return self.api_key

    def get_cache_ttl(self) -> int:
        """Get the current cache TTL (in seconds).

        Returns:
            int: The current cache TTL.
        """

        return self.cache_ttl

    def get_cache_enabled(self) -> bool:
        """Get the current cache enabled.

        Returns:
            bool: The current cache enabled.
        """

        return self.cache_ttl
