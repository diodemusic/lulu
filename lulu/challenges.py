import utils


def config(region: str) -> list[object]:
    """List of all basic challenge configuration information (includes all translations for names and descriptions).

    Args:
        region (str): Region str.

    Returns:
        list: List of ChallengeConfigInfo objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/config"
    )

    for item in r:
        thresholds_data = item["thresholds"]

        entry = utils.classes.ChallengeConfigInfo(
            challenge_id=item["id"],
            leaderboard=item["leaderboard"],
            localized_names=item["localizedNames"],
            state=item["state"],
            thresholds=utils.classes.Thresholds(
                iron=thresholds_data.get("IRON", 0),
                bronze=thresholds_data.get("BRONZE", 0),
                silver=thresholds_data.get("SILVER", 0),
                gold=thresholds_data.get("GOLD", 0),
                platinum=thresholds_data.get("PLATINUM", 0),
                diamond=thresholds_data.get("DIAMOND", 0),
                master=thresholds_data.get("MASTER", 0),
                grandmaster=thresholds_data.get("GRANDMASTER", 0),
                challenger=thresholds_data.get("CHALLENGER", 0),
            ),
            tracking=item.get("tracking", ""),
            start_timestamp=item.get("startTimeStamp", 0),
            end_timestamp=item.get("endTimestamp", 0),
        )

        entries.append(entry)

    return entries


def percentiles(region: str) -> dict:
    """Dict of id: level to percentile of players who have achieved it.

    Args:
        region (str): Region str.

    Returns:
        dict: Percentiles dictionary: {id: Percentiles}.
    """

    percentiles = {}

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/percentiles"
    )

    for key in r:
        percentiles[key] = utils.classes.Percentiles(
            iron=r[key].get("IRON", 0),
            bronze=r[key].get("BRONZE", 0),
            silver=r[key].get("SILVER", 0),
            gold=r[key].get("GOLD", 0),
            platinum=r[key].get("PLATINUM", 0),
            diamond=r[key].get("DIAMOND", 0),
            master=r[key].get("MASTER", 0),
            grandmaster=r[key].get("GRANDMASTER", 0),
            challenger=r[key].get("CHALLENGER", 0),
        )

    return percentiles


def config_by_challenge_id(region: str, challenge_id: int) -> object:
    """Get challenge configuration (REST).

    Args:
        region (str): Region str.
        challenge_id (int): Challenge ID.

    Returns:
        object: ChallengeConfigInfo object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/config"
    )

    thresholds_data = r["thresholds"]

    return utils.classes.ChallengeConfigInfo(
        challenge_id=r["id"],
        leaderboard=r["leaderboard"],
        localized_names=r["localizedNames"],
        state=r["state"],
        thresholds=utils.classes.Thresholds(
            iron=thresholds_data.get("IRON", 0),
            bronze=thresholds_data.get("BRONZE", 0),
            silver=thresholds_data.get("SILVER", 0),
            gold=thresholds_data.get("GOLD", 0),
            platinum=thresholds_data.get("PLATINUM", 0),
            diamond=thresholds_data.get("DIAMOND", 0),
            master=thresholds_data.get("MASTER", 0),
            grandmaster=thresholds_data.get("GRANDMASTER", 0),
            challenger=thresholds_data.get("CHALLENGER", 0),
        ),
        tracking=r.get("tracking", ""),
        start_timestamp=r.get("startTimeStamp", 0),
        end_timestamp=r.get("endTimestamp", 0),
    )


def apex_players(region: str, challenge_id: int, level: str) -> list:
    """Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER.

    Args:
        region (str): Region str.
        challenge_id (int): Challenge ID.
        level (str): Level str.

    Returns:
        list: List of ApexPlayerInfo objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level}"
    )

    for item in r:
        entry = utils.classes.ApexPlayerInfo(
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

    challenges_lst = []

    for challenge in r["challenges"]:
        challenges_lst.append(
            utils.classes.ChallengeInfo(
                achieved_time=challenge.get("achievedTime", 0),
                challenge_id=challenge["challengeId"],
                level=challenge["level"],
                percentile=challenge["percentile"],
                value=challenge["value"],
            )
        )

    return utils.classes.PlayerInfo(
        category_points=utils.classes.CategoryPoints(
            collection=utils.classes.Collection(
                current=r["categoryPoints"]["COLLECTION"]["current"],
                level=r["categoryPoints"]["COLLECTION"]["level"],
                max=r["categoryPoints"]["COLLECTION"]["max"],
                percentile=r["categoryPoints"]["COLLECTION"]["percentile"],
            ),
            expertise=utils.classes.Expertise(
                current=r["categoryPoints"]["EXPERTISE"]["current"],
                level=r["categoryPoints"]["EXPERTISE"]["level"],
                max=r["categoryPoints"]["EXPERTISE"]["max"],
                percentile=r["categoryPoints"]["EXPERTISE"]["percentile"],
            ),
            imagination=utils.classes.Imagination(
                current=r["categoryPoints"]["IMAGINATION"]["current"],
                level=r["categoryPoints"]["IMAGINATION"]["level"],
                max=r["categoryPoints"]["IMAGINATION"]["max"],
                percentile=r["categoryPoints"]["IMAGINATION"]["percentile"],
            ),
            teamwork=utils.classes.Teamwork(
                current=r["categoryPoints"]["TEAMWORK"]["current"],
                level=r["categoryPoints"]["TEAMWORK"]["level"],
                max=r["categoryPoints"]["TEAMWORK"]["max"],
                percentile=r["categoryPoints"]["TEAMWORK"]["percentile"],
            ),
            veterancy=utils.classes.Veterancy(
                current=r["categoryPoints"]["VETERANCY"]["current"],
                level=r["categoryPoints"]["VETERANCY"]["level"],
                max=r["categoryPoints"]["VETERANCY"]["max"],
                percentile=r["categoryPoints"]["VETERANCY"]["percentile"],
            ),
        ),
        challenges=challenges_lst,
        preferences=utils.classes.PlayerClientPreferences(
            banner_accent=r["preferences"]["bannerAccent"],
            challenge_ids=r["preferences"]["challengeIds"],
            crest_border=r["preferences"]["crestBorder"],
            prestige_crest_border_level=r["preferences"]["prestigeCrestBorderLevel"],
            title=r["preferences"]["title"],
        ),
        total_points=utils.classes.ChallengePoints(
            current=r["totalPoints"]["current"],
            level=r["totalPoints"]["level"],
            max=r["totalPoints"]["max"],
            percentile=r["totalPoints"]["percentile"],
        ),
    )
