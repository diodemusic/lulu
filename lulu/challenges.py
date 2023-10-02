import utils


def config(region: str) -> list:
    """List of all basic challenge configuration information (includes all translations for names and descriptions).

    Args:
        region (str): Region str.

    Returns:
        list: List of ChallengeConfig objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/config"
    )

    for item in r:
        entry = utils.classes.ChallengeConfig(
            challenge_id=item["id"],
            leaderboard=item["leaderboard"],
            localized_names=item["localizedNames"],
            state=item["state"],
            thresholds=item["thresholds"],
        )

        entries.append(entry)

    return entries


def percentiles(region: str) -> dict:
    """Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it.

    Args:
        region (str): Region str.

    Returns:
        dict: Percentiles dictionary.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/percentiles"
    )

    return r


def config_by_challenge_id(region: str, challenge_id: int) -> object:
    """Get challenge configuration (REST).

    Args:
        region (str): Region str.
        challenge_id (int): Challenge ID.

    Returns:
        object: ChallengeConfig object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/config"
    )

    return utils.classes.ChallengeConfig(
        challenge_id=r["id"],
        leaderboard=r["leaderboard"],
        localized_names=r["localizedNames"],
        state=r["state"],
        thresholds=r["thresholds"],
    )


def apex_players(region: str, challenge_id: int, level: str) -> list:
    """Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER.

    Args:
        region (str): Region str.
        challenge_id (int): Challenge ID.
        level (str): Level str.

    Returns:
        list: List of ApexPlayersInfo objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level}"
    )

    for item in r:
        entry = utils.classes.ApexPlayersInfo(
            position=item["position"],
            puuid=item["puuid"],
            value=item["value"],
        )

        entries.append(entry)

    return entries


def percentiles_by_challenge_id(region: str, challenge_id: int) -> object:
    """Map of level to percentile of players who have achieved it.

    Args:
        region (str): Region str.
        challenge_id (int): Challenge ID.

    Returns:
        object: Percentiles object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/percentiles"
    )

    return utils.classes.Percentiles(
        iron=r["IRON"],
        bronze=r["BRONZE"],
        silver=r["SILVER"],
        gold=r["GOLD"],
        platinum=r["PLATINUM"],
        diamond=r["DIAMOND"],
        master=r["MASTER"],
        grandmaster=r["GRANDMASTER"],
        challenger=r["CHALLENGER"],
        none=r["NONE"],
    )


def by_puuid(region: str, puuid: str) -> object:
    """Returns player information with list of all progressed challenges (REST).

    Args:
        region (str): Region str.
        puuid (str): Puuid.

    Returns:
        object: PlayerInfo object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/player-data/{puuid}"
    )

    return utils.classes.PlayerInfo(
        category_points=r["categoryPoints"],
        challenges=r["challenges"],
        preferences=r["preferences"],
        total_points=r["totalPoints"],
    )
