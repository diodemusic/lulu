import utils


def by_summoner_id(region: str, summoner_id: str) -> object:
    """Get current game information for the given summoner ID.

    Args:
        key (str): Riot API key
        region (str): Region str
        summoner_id (str): Summoner ID

    Returns:
        object: Spectator object
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}"
    )

    return utils.classes.Spectator(
        banned_champions=r["bannedChampions"],
        game_id=r["gameId"],
        length=r["gameLength"],
        mode=r["gameMode"],
        queue_config_id=r["gameQueueConfigId"],
        start_time=r["gameStartTime"],
        game_type=r["gameType"],
        map_id=r["mapId"],
        observers=r["observers"],
        participants=r["participants"],
        platform_id=r["platformId"],
    )


def featured_games(region: str) -> object:
    """Get list of featured games.

    Args:
        key (str): Riot API key
        region (str): Region str

    Returns:
        object: FeaturedGames object
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/spectator/v4/featured-games"
    )

    return utils.classes.FeaturedGames(
        client_refresh_interval=r["clientRefreshInterval"], game_list=r["gameList"]
    )
