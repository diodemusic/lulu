"""
The **endpoints** submodule defines classes and functions that interact directly with Riot's REST API endpoints.

Each file in this package corresponds to a specific Riot API service — such as Summoner, Match, League, or Champion Mastery — and provides convenient wrapper functions for requesting and parsing data.

**Typical usage:**

    from pyke import Continent, Pyke, exceptions

    api = Pyke("API_KEY", print_url=False)

    account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")
"""
