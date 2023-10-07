import utils


def challenger_leagues_by_queue(region: str, queue: str) -> object:
    """Get the challenger league for given queue.

    Args:
        region (str): Region str.
        queue (str): Queue str.

    Returns:
        object: LeagueList object.
    """

    league_entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue}"
    )

    for entry in r["entries"]:
        mini_series_data = entry.get("miniSeries", {})
        league_entries.append(
            utils.classes.LeagueItem(
                summoner_id=entry["summonerId"],
                summoner_name=entry["summonerName"],
                mini_series=utils.classes.MiniSeries(
                    losses=mini_series_data.get("losses", 0),
                    progress=mini_series_data.get("progress", ""),
                    target=mini_series_data.get("target", 0),
                    wins=mini_series_data.get("wins", 0),
                ),
                league_points=entry.get("leaguePoints", 0),
                rank=entry.get("rank", ""),
                wins=entry.get("wins", 0),
                losses=entry.get("losses", 0),
                veteran=entry.get("veteran", False),
                inactive=entry.get("inactive", False),
                fresh_blood=entry.get("freshBlood", False),
                hot_streak=entry.get("hotStreak", False),
            )
        )

    return utils.classes.LeagueList(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=league_entries,
    )


def by_summoner(region: str, summoner_id: str) -> list:
    """Get league entries in all queues for a given summoner ID.

    Args:
        region (str): Region str.
        summoner_id (str): Summoner ID.

    Returns:
        list: List of LeagueEntry objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
    )

    for item in r:
        mini_series_data = item.get("miniSeries", {})
        entry = utils.classes.LeagueEntry(
            fresh_blood=item["freshBlood"],
            hot_streak=item["hotStreak"],
            inactive=item["inactive"],
            league_id=item["leagueId"],
            league_points=item["leaguePoints"],
            losses=item["losses"],
            queue_type=item["queueType"],
            rank=item["rank"],
            summoner_id=item["summonerId"],
            summoner_name=item["summonerName"],
            tier=item["tier"],
            veteran=item["veteran"],
            wins=item["wins"],
            mini_series=utils.classes.MiniSeries(
                losses=mini_series_data.get("losses", 0),
                progress=mini_series_data.get("progress", ""),
                target=mini_series_data.get("target", 0),
                wins=mini_series_data.get("wins", 0),
            ),
        )

        entries.append(entry)

    return entries


def by_queue_tier_division(
    region: str,
    queue: str,
    tier: str,
    division: str,
    page: int = 1,
) -> list:
    """Get all the league entries.

    Args:
        region (str): Region str.
        queue (str): Queue str.
        tier (str): Ranked tier str.
        division (str): Ranked division str.
        page (int): Page of entries to retrieve.

    Returns:
        list: List of LeagueEntry objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/entries/{queue}/{tier}/{division}?page={page}"
    )

    for item in r:
        mini_series_data = item.get("miniSeries", {})
        entry = utils.classes.LeagueEntry(
            fresh_blood=item["freshBlood"],
            hot_streak=item["hotStreak"],
            inactive=item["inactive"],
            league_id=item["leagueId"],
            league_points=item["leaguePoints"],
            losses=item["losses"],
            queue_type=item["queueType"],
            rank=item["rank"],
            summoner_id=item["summonerId"],
            summoner_name=item["summonerName"],
            tier=item["tier"],
            veteran=item["veteran"],
            wins=item["wins"],
            mini_series=utils.classes.MiniSeries(
                losses=mini_series_data.get("losses", 0),
                progress=mini_series_data.get("progress", ""),
                target=mini_series_data.get("target", 0),
                wins=mini_series_data.get("wins", 0),
            ),
        )

        entries.append(entry)

    return entries


def grandmaster_leagues_by_queue(region: str, queue: str) -> object:
    """Get the grandmaster league for given queue.

    Args:
        region (str): Region str.
        queue (str): Queue str.

    Returns:
        object: LeagueList object.
    """

    league_entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue}"
    )

    for entry in r["entries"]:
        mini_series_data = entry.get("miniSeries", {})
        league_entries.append(
            utils.classes.LeagueItem(
                summoner_id=entry["summonerId"],
                summoner_name=entry["summonerName"],
                mini_series=utils.classes.MiniSeries(
                    losses=mini_series_data.get("losses", 0),
                    progress=mini_series_data.get("progress", ""),
                    target=mini_series_data.get("target", 0),
                    wins=mini_series_data.get("wins", 0),
                ),
                league_points=entry.get("leaguePoints", 0),
                rank=entry.get("rank", ""),
                wins=entry.get("wins", 0),
                losses=entry.get("losses", 0),
                veteran=entry.get("veteran", False),
                inactive=entry.get("inactive", False),
                fresh_blood=entry.get("freshBlood", False),
                hot_streak=entry.get("hotStreak", False),
            )
        )

    return utils.classes.LeagueList(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=league_entries,
    )


def by_league_id(region: str, league_id: str) -> object:
    """Get league with given ID, including inactive entries.

    Args:
        region (str): Region str.
        league_id (str): League ID.

    Returns:
        object: LeagueList object.
    """

    league_entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/leagues/{league_id}"
    )

    for entry in r["entries"]:
        mini_series_data = entry.get("miniSeries", {})
        league_entries.append(
            utils.classes.LeagueItem(
                summoner_id=entry["summonerId"],
                summoner_name=entry["summonerName"],
                mini_series=utils.classes.MiniSeries(
                    losses=mini_series_data.get("losses", 0),
                    progress=mini_series_data.get("progress", ""),
                    target=mini_series_data.get("target", 0),
                    wins=mini_series_data.get("wins", 0),
                ),
                league_points=entry.get("leaguePoints", 0),
                rank=entry.get("rank", ""),
                wins=entry.get("wins", 0),
                losses=entry.get("losses", 0),
                veteran=entry.get("veteran", False),
                inactive=entry.get("inactive", False),
                fresh_blood=entry.get("freshBlood", False),
                hot_streak=entry.get("hotStreak", False),
            )
        )

    return utils.classes.LeagueList(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=league_entries,
    )


def master_leagues_by_queue(region: str, queue: str) -> object:
    """Get the master league for given queue.

    Args:
        region (str): Region str.
        queue (str): Queue str.

    Returns:
        object: LeagueList object.
    """

    league_entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue}"
    )

    for entry in r["entries"]:
        mini_series_data = entry.get("miniSeries", {})
        league_entries.append(
            utils.classes.LeagueItem(
                summoner_id=entry["summonerId"],
                summoner_name=entry["summonerName"],
                mini_series=utils.classes.MiniSeries(
                    losses=mini_series_data.get("losses", 0),
                    progress=mini_series_data.get("progress", ""),
                    target=mini_series_data.get("target", 0),
                    wins=mini_series_data.get("wins", 0),
                ),
                league_points=entry.get("leaguePoints", 0),
                rank=entry.get("rank", ""),
                wins=entry.get("wins", 0),
                losses=entry.get("losses", 0),
                veteran=entry.get("veteran", False),
                inactive=entry.get("inactive", False),
                fresh_blood=entry.get("freshBlood", False),
                hot_streak=entry.get("hotStreak", False),
            )
        )

    return utils.classes.LeagueList(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=league_entries,
    )
