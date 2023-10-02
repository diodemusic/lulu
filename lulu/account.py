from . import __utils


def by_puuid(key: str, continent: str, puuid: str) -> object:
    """Get account by puuid.

    Args:
        key (str): Riot API key.
        continent (str): Continent str.
        puuid (str): Puuid.

    Returns:
        object: Account object.
    """

    r = __utils.call(
        url=f"https://{continent}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}",
        key=key,
    )

    return __utils.Account(
        puuid=r["puuid"], game_name=r["gameName"], tag_line=r["tagLine"]
    )


def by_riot_id(key: str, continent: str, game_name: str, tag_line: str) -> object:
    """Get account by riot ID.

    Args:
        key (str): Riot API key.
        continent (str): Continent str.
        game_name (str): In game name.
        tag_line (str): In game tag line.

    Returns:
        object: Account object.
    """

    r = __utils.call(
        url=f"https://{continent}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}",
        key=key,
    )

    return __utils.Account(
        puuid=r["puuid"], game_name=r["gameName"], tag_line=r["tagLine"]
    )
