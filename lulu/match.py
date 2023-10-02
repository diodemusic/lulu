from . import __utils


def history(
    key: str,
    continent: str,
    puuid: str,
    queue: int,
    start: int = 0,
    count: int = 20,
) -> list:
    """Get a list of match ids by puuid.

    Args:
        key (str): Riot API key.
        continent (str): Continent str.
        puuid (str): Puuid.
        queue (int): Queue ID
        start (int, optional): Start index. Defaults to 0.
        count (int, optional): Valid values: 0 to 100. Number of match IDs to return. Defaults to 20.

    Returns:
        list: List of match IDs.
    """

    r = __utils.call(
        url=f"https://{continent}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue={queue}&start={start}&count={count}",
        key=key,
    )

    return r


def by_match_id(key: str, continent: str, match_id: str) -> object:
    """Get a match by match id.

    Args:
        key (str): Riot API key.
        continent (str): Continent str.
        match_id (str): Match ID.

    Returns:
        object: Match object.
    """

    r = __utils.call(
        url=f"https://{continent}.api.riotgames.com/lol/match/v5/matches/{match_id}",
        key=key,
    )

    info = r["info"]
    metadata = r["metadata"]

    return __utils.Match(
        info=__utils.MatchInfo(
            creation=info["gameCreation"],
            duration=info["gameDuration"],
            end_timestamp=info["gameEndTimestamp"],
            game_id=info["gameId"],
            mode=info["gameMode"],
            name=info["gameName"],
            start_timestamp=info["gameStartTimestamp"],
            game_type=info["gameType"],
            version=info["gameVersion"],
            map_id=info["mapId"],
            participants=info["participants"],
            platform_id=info["platformId"],
            queue_id=info["queueId"],
            teams=info["teams"],
            tournament_code=info["tournamentCode"],
        ),
        metadata=__utils.Metadata(
            data_version=metadata["dataVersion"],
            match_id=metadata["matchId"],
            participants=metadata["participants"],
        ),
    )


def timeline_by_match_id(key: str, continent: str, match_id: str) -> object:
    """Get a match timeline by match id.

    Args:
        key (str): Riot API key.
        continent (str): Continent str.
        match_id (str): Match ID

    Returns:
        object: MatchTimeline object.
    """

    r = __utils.call(
        url=f"https://{continent}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline",
        key=key,
    )

    info = r["info"]
    metadata = r["metadata"]

    return __utils.MatchTimeline(
        info=__utils.TimelineInfo(
            frame_interval=info["frameInterval"],
            frames=info["frames"],
            game_id=info["gameId"],
            participants=info["participants"],
        ),
        metadata=__utils.Metadata(
            data_version=metadata["dataVersion"],
            match_id=metadata["matchId"],
            participants=metadata["participants"],
        ),
    )
