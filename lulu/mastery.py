from . import __utils


def by_puuid(key: str, region: str, puuid: str) -> list:
    """Get all champion mastery entries sorted by number of champion points descending.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        puuid (str): Puuid.

    Returns:
        list: List of MasteryEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}",
        key=key,
    )

    for item in r:
        entry = __utils.MasteryEntry(
            puuid=item["puuid"],
            champion_id=item["championId"],
            level=item["championLevel"],
            points=item["championPoints"],
            last_play_time=item["lastPlayTime"],
            points_since_last_level=item["championPointsSinceLastLevel"],
            points_until_next_level=item["championPointsUntilNextLevel"],
            chest_granted=item["chestGranted"],
            tokens_earned=item["tokensEarned"],
            summoner_id=item["summonerId"],
        )

        entries.append(entry)

    return entries


def by_puuid_and_champion_id(
    key: str, region: str, puuid: str, champion_id: int
) -> object:
    """Get a champion mastery by puuid and champion ID.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        puuid (str): Puuid.
        champion_id (int): Champion id.

    Returns:
        object: MasteryEntry object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}",
        key=key,
    )

    return __utils.MasteryEntry(
        puuid=r["puuid"],
        champion_id=r["championId"],
        level=r["championLevel"],
        points=r["championPoints"],
        last_play_time=r["lastPlayTime"],
        points_since_last_level=r["championPointsSinceLastLevel"],
        points_until_next_level=r["championPointsUntilNextLevel"],
        chest_granted=r["chestGranted"],
        tokens_earned=r["tokensEarned"],
        summoner_id=r["summonerId"],
    )


def by_puuid_top(key: str, region: str, puuid: str, count: str = 3):
    """Get specified number of top champion mastery entries sorted by number of champion points descending.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        puuid (str): Puuid.
        count (str, optional): Count of mastery entries to get. Defaults to 3.

    Returns:
        list: List of MasteryEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count={count}",
        key=key,
    )

    for item in r:
        entry = __utils.MasteryEntry(
            puuid=item["puuid"],
            champion_id=item["championId"],
            level=item["championLevel"],
            points=item["championPoints"],
            last_play_time=item["lastPlayTime"],
            points_since_last_level=item["championPointsSinceLastLevel"],
            points_until_next_level=item["championPointsUntilNextLevel"],
            chest_granted=item["chestGranted"],
            tokens_earned=item["tokensEarned"],
            summoner_id=item["summonerId"],
        )

        entries.append(entry)

    return entries


def by_summoner_id(key: str, region: str, summoner_id: str) -> list:
    """Get all champion mastery entries sorted by number of champion points descending.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        summoner_id (str): Summoner ID.

    Returns:
        list: List of MasteryEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}",
        key=key,
    )

    for item in r:
        entry = __utils.MasteryEntry(
            puuid=item["puuid"],
            champion_id=item["championId"],
            level=item["championLevel"],
            points=item["championPoints"],
            last_play_time=item["lastPlayTime"],
            points_since_last_level=item["championPointsSinceLastLevel"],
            points_until_next_level=item["championPointsUntilNextLevel"],
            chest_granted=item["chestGranted"],
            tokens_earned=item["tokensEarned"],
            summoner_id=item["summonerId"],
        )
        entries.append(entry)

    return entries


def by_summoner_id_and_champion_id(
    key: str, region: str, summoner_id: str, champion_id: int
) -> object:
    """Get a champion mastery by Summoner ID and champion ID.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        summoner_id (str): Summoner ID.
        champion_id (int): Champion ID.

    Returns:
        object: MasteryEntry object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}",
        key=key,
    )

    return __utils.MasteryEntry(
        puuid=r["puuid"],
        champion_id=r["championId"],
        level=r["championLevel"],
        points=r["championPoints"],
        last_play_time=r["lastPlayTime"],
        points_since_last_level=r["championPointsSinceLastLevel"],
        points_until_next_level=r["championPointsUntilNextLevel"],
        chest_granted=r["chestGranted"],
        tokens_earned=r["tokensEarned"],
        summoner_id=r["summonerId"],
    )


def by_summoner_id_top(key: str, region: str, summoner_id: str, count: str = 3):
    """Get specified number of top champion mastery entries sorted by number of champion points descending.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        summoner_id (str): Summoner ID.
        count (str, optional): Count of mastery entries to get. Defaults to 3.

    Returns:
        list: List of MasteryEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/top?count={count}",
        key=key,
    )

    for item in r:
        entry = __utils.MasteryEntry(
            puuid=item["puuid"],
            champion_id=item["championId"],
            level=item["championLevel"],
            points=item["championPoints"],
            last_play_time=item["lastPlayTime"],
            points_since_last_level=item["championPointsSinceLastLevel"],
            points_until_next_level=item["championPointsUntilNextLevel"],
            chest_granted=item["chestGranted"],
            tokens_earned=item["tokensEarned"],
            summoner_id=item["summonerId"],
        )

        entries.append(entry)

    return entries


def levels_sum_by_puuid(key: str, region: str, puuid: str):
    """Get a player's total champion mastery score, which is the sum of individual champion mastery levels.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        puuid (str): Puuid.

    Returns:
        int: Sum of mastery levels int.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/{puuid}",
        key=key,
    )

    return r


def levels_sum_by_summoner_id(key: str, region: str, summoner_id: str):
    """Get a player's total champion mastery score, which is the sum of individual champion mastery levels.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        summoner_id (str): Summoner ID.

    Returns:
        int: Sum of mastery levels int.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{summoner_id}",
        key=key,
    )

    return r
