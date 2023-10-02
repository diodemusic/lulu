from . import __utils


def challenger(key: str, region: str, queue: str) -> object:
    """Get the challenger league for given queue.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        queue (str): Queue str.

    Returns:
        object: League object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue}",
        key=key,
    )

    return __utils.League(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=r["entries"],
    )


def by_summoner_id(key: str, region: str, summoner_id: str) -> list:
    """Get league entries in all queues for a given summoner ID.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        summoner_id (str): Summoner ID.

    Returns:
        list: List of LeagueEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}",
        key=key,
    )

    for item in r:
        entry = __utils.LeagueEntry(
            fresh_blood=item["freshBlood"],
            hot_streak=item["hotStreak"],
            inactive=item["inactive"],
            league_id=item["leagueId"],
            points=item["leaguePoints"],
            losses=item["losses"],
            queue_type=item["queueType"],
            rank=item["rank"],
            summoner_id=item["summonerId"],
            summoner_name=item["summonerName"],
            tier=item["tier"],
            veteran=item["veteran"],
            wins=item["wins"],
        )

        entries.append(entry)

    return entries


def by_queue_tier_division(
    key: str,
    region: str,
    queue: str,
    tier: str,
    division: str,
    page: int = 1,
) -> list:
    """Get all the league entries.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        queue (str): Queue str.
        tier (str): Ranked tier str.
        division (str): Ranked division str.
        page (int): Page of entries to retrieve.

    Returns:
        list: List of LeagueEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/entries/{queue}/{tier}/{division}?page={page}",
        key=key,
    )

    for item in r:
        entry = __utils.LeagueEntry(
            fresh_blood=item["freshBlood"],
            hot_streak=item["hotStreak"],
            inactive=item["inactive"],
            league_id=item["leagueId"],
            points=item["leaguePoints"],
            losses=item["losses"],
            queue_type=item["queueType"],
            rank=item["rank"],
            summoner_id=item["summonerId"],
            summoner_name=item["summonerName"],
            tier=item["tier"],
            veteran=item["veteran"],
            wins=item["wins"],
        )

        entries.append(entry)

    return entries


def grandmaster(key: str, region: str, queue: str) -> object:
    """Get the grandmaster league for given queue.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        queue (str): Queue str.

    Returns:
        object: League object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue}",
        key=key,
    )

    return __utils.League(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=r["entries"],
    )


def by_league_id(key: str, region: str, league_id: str) -> object:
    """Get league with given ID, including inactive entries.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        league_id (str): League ID.

    Returns:
        object: League object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/leagues/{league_id}",
        key=key,
    )

    return __utils.League(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=r["entries"],
    )


def master(key: str, region: str, queue: str) -> object:
    """Get the master league for given queue.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        queue (str): Queue str.

    Returns:
        object: League object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue}",
        key=key,
    )

    return __utils.League(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=r["entries"],
    )
