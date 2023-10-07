import utils


def by_puuid(region: str, puuid: str) -> list:
    """Get all champion mastery entries sorted by number of champion points descending.

    Args:
        region (str): Region str.
        puuid (str): Puuid.

    Returns:
        list: List of ChampionMastery objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
    )

    for item in r:
        entry = utils.classes.ChampionMastery(
            puuid=item["puuid"],
            champion_id=item["championId"],
            champion_level=item["championLevel"],
            champion_points=item["championPoints"],
            last_play_time=item["lastPlayTime"],
            champion_points_since_last_level=item["championPointsSinceLastLevel"],
            champion_points_until_next_level=item["championPointsUntilNextLevel"],
            chest_granted=item["chestGranted"],
            tokens_earned=item["tokensEarned"],
            summoner_id=item["summonerId"],
        )

        entries.append(entry)

    return entries


def by_puuid_and_champion(region: str, puuid: str, champion_id: int) -> object:
    """Get a champion mastery by puuid and champion ID.

    Args:
        region (str): Region str.
        puuid (str): Puuid.
        champion_id (int): Champion id.

    Returns:
        object: ChampionMastery object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
    )

    return utils.classes.ChampionMastery(
        puuid=r["puuid"],
        champion_id=r["championId"],
        champion_level=r["championLevel"],
        champion_points=r["championPoints"],
        last_play_time=r["lastPlayTime"],
        champion_points_since_last_level=r["championPointsSinceLastLevel"],
        champion_points_until_next_level=r["championPointsUntilNextLevel"],
        chest_granted=r["chestGranted"],
        tokens_earned=r["tokensEarned"],
        summoner_id=r["summonerId"],
    )


def by_puuid_top(region: str, puuid: str, count: str = 3):
    """Get specified number of top champion mastery entries sorted by number of champion points descending.

    Args:
        region (str): Region str.
        puuid (str): Puuid.
        count (str, optional): Count of mastery entries to get. Defaults to 3.

    Returns:
        list: List of ChampionMastery objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count={count}"
    )

    for item in r:
        entry = utils.classes.ChampionMastery(
            puuid=item["puuid"],
            champion_id=item["championId"],
            champion_level=item["championLevel"],
            champion_points=item["championPoints"],
            last_play_time=item["lastPlayTime"],
            champion_points_since_last_level=item["championPointsSinceLastLevel"],
            champion_points_until_next_level=item["championPointsUntilNextLevel"],
            chest_granted=item["chestGranted"],
            tokens_earned=item["tokensEarned"],
            summoner_id=item["summonerId"],
        )

        entries.append(entry)

    return entries


def by_summoner(region: str, summoner_id: str) -> list:
    """Get all champion mastery entries sorted by number of champion points descending.

    Args:
        region (str): Region str.
        summoner_id (str): Summoner ID.

    Returns:
        list: List of ChampionMastery objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}"
    )

    for item in r:
        entry = utils.classes.ChampionMastery(
            puuid=item["puuid"],
            champion_id=item["championId"],
            champion_level=item["championLevel"],
            champion_points=item["championPoints"],
            last_play_time=item["lastPlayTime"],
            champion_points_since_last_level=item["championPointsSinceLastLevel"],
            champion_points_until_next_level=item["championPointsUntilNextLevel"],
            chest_granted=item["chestGranted"],
            tokens_earned=item["tokensEarned"],
            summoner_id=item["summonerId"],
        )
        entries.append(entry)

    return entries


def by_summoner_and_champion(region: str, summoner_id: str, champion_id: int) -> object:
    """Get a champion mastery by Summoner ID and champion ID.

    Args:
        region (str): Region str.
        summoner_id (str): Summoner ID.
        champion_id (int): Champion ID.

    Returns:
        object: ChampionMastery object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}"
    )

    return utils.classes.ChampionMastery(
        puuid=r["puuid"],
        champion_id=r["championId"],
        champion_level=r["championLevel"],
        champion_points=r["championPoints"],
        last_play_time=r["lastPlayTime"],
        champion_points_since_last_level=r["championPointsSinceLastLevel"],
        champion_points_until_next_level=r["championPointsUntilNextLevel"],
        chest_granted=r["chestGranted"],
        tokens_earned=r["tokensEarned"],
        summoner_id=r["summonerId"],
    )


def by_summoner_top(region: str, summoner_id: str, count: str = 3):
    """Get specified number of top champion mastery entries sorted by number of champion points descending.

    Args:
        region (str): Region str.
        summoner_id (str): Summoner ID.
        count (str, optional): Count of mastery entries to get. Defaults to 3.

    Returns:
        list: List of ChampionMastery objects.
    """

    entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/top?count={count}"
    )

    for item in r:
        entry = utils.classes.ChampionMastery(
            puuid=item["puuid"],
            champion_id=item["championId"],
            champion_level=item["championLevel"],
            champion_points=item["championPoints"],
            last_play_time=item["lastPlayTime"],
            champion_points_since_last_level=item["championPointsSinceLastLevel"],
            champion_points_until_next_level=item["championPointsUntilNextLevel"],
            chest_granted=item["chestGranted"],
            tokens_earned=item["tokensEarned"],
            summoner_id=item["summonerId"],
        )

        entries.append(entry)

    return entries


def scores_by_puuid(region: str, puuid: str):
    """Get a player's total champion mastery score, which is the sum of individual champion mastery levels.

    Args:
        region (str): Region str.
        puuid (str): Puuid.

    Returns:
        int: Sum of mastery levels int.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/{puuid}"
    )

    return r


def scores_by_summoner(region: str, summoner_id: str):
    """Get a player's total champion mastery score, which is the sum of individual champion mastery levels.

    Args:
        region (str): Region str.
        summoner_id (str): Summoner ID.

    Returns:
        int: Sum of mastery levels int.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{summoner_id}"
    )

    return r
