from enum import Enum as __Enum
from .private import __utils


class continent(__Enum):
    americas = "americas"
    asia = "asia"
    esports = "esports"
    europe = "europe"


class region(__Enum):
    na = "na1"
    euw = "euw1"
    eune = "eun1"
    br = "br1"
    lan = "la1"
    las = "la2"
    kr = "kr"
    oce = "oc1"
    tr = "tr1"
    ru = "ru"
    jp = "jp1"


class queue(__Enum):
    solo_duo = "RANKED_SOLO_5x5"
    flex = "RANKED_FLEX_SR"


class tier(__Enum):
    iron = "IRON"
    bronze = "BRONZE"
    silver = "SILVER"
    gold = "GOLD"
    platinum = "PLATINUM"
    emerald = "EMERALD"
    diamond = "DIAMOND"


class division(__Enum):
    one = "I"
    two = "II"
    three = "III"
    four = "IV"


class level(__Enum):
    master = "MASTER"
    grandmaster = "GRANDMASTER"
    challenger = "CHALLENGER"


def account_by_puuid(key: str, continent: continent, puuid: str) -> object:
    """Get account by puuid.

    Args:
        key (str): Riot API key.
        continent (enum): Continent enum.
        puuid (str): Puuid.

    Returns:
        object: Account object.
    """

    r = __utils.call(
        url=f"https://{continent.value}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}",
        key=key,
    )

    return __utils.Account(
        puuid=r["puuid"], game_name=r["gameName"], tag_line=r["tagLine"]
    )


def account_by_riot_id(
    key: str, continent: continent, game_name: str, tag_line: str
) -> object:
    """Get account by riot ID.

    Args:
        key (str): Riot API key.
        continent (enum): Continent enum.
        game_name (str): In game name.
        tag_line (str): In game tag line.

    Returns:
        object: Account object.
    """

    r = __utils.call(
        url=f"https://{continent.value}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}",
        key=key,
    )

    return __utils.Account(
        puuid=r["puuid"], game_name=r["gameName"], tag_line=r["tagLine"]
    )


def mastery_by_puuid(key: str, region: region, puuid: str) -> list:
    """Get all champion mastery entries sorted by number of champion points descending.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        puuid (str): Puuid.

    Returns:
        list: List of MasteryEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}",
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


def mastery_by_puuid_and_champion_id(
    key: str, region: region, puuid: str, champion_id: int
) -> object:
    """Get a champion mastery by puuid and champion ID.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        puuid (str): Puuid.
        champion_id (int): Champion id.

    Returns:
        object: MasteryEntry object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}",
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


def mastery_by_puuid_top(key: str, region: region, puuid: str, count: str = 3):
    """Get specified number of top champion mastery entries sorted by number of champion points descending.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        puuid (str): Puuid.
        count (str, optional): Count of mastery entries to get. Defaults to 3.

    Returns:
        list: List of MasteryEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count={count}",
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


def mastery_by_summoner_id(key: str, region: region, summoner_id: str) -> list:
    """Get all champion mastery entries sorted by number of champion points descending.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        summoner_id (str): Summoner ID.

    Returns:
        list: List of MasteryEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}",
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


def mastery_by_summoner_id_and_champion_id(
    key: str, region: region, summoner_id: str, champion_id: int
) -> object:
    """Get a champion mastery by Summoner ID and champion ID.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        summoner_id (str): Summoner ID.
        champion_id (int): Champion ID.

    Returns:
        object: MasteryEntry object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}",
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


def mastery_by_summoner_id_top(
    key: str, region: region, summoner_id: str, count: str = 3
):
    """Get specified number of top champion mastery entries sorted by number of champion points descending.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        summoner_id (str): Summoner ID.
        count (str, optional): Count of mastery entries to get. Defaults to 3.

    Returns:
        list: List of MasteryEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/top?count={count}",
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


def mastery_levels_sum_by_puuid(key: str, region: region, puuid: str):
    """Get a player's total champion mastery score, which is the sum of individual champion mastery levels.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        puuid (str): Puuid.

    Returns:
        int: Sum of mastery levels int.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/{puuid}",
        key=key,
    )

    return r


def mastery_levels_sum_by_summoner_id(key: str, region: region, summoner_id: str):
    """Get a player's total champion mastery score, which is the sum of individual champion mastery levels.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        summoner_id (str): Summoner ID.

    Returns:
        int: Sum of mastery levels int.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{summoner_id}",
        key=key,
    )

    return r


def champion_free_rotation(key: str, region: region) -> object:
    """Returns champion rotations, including free-to-play and low-level free-to-play rotations.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.

    Returns:
        object: FreeChampionRotation object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/platform/v3/champion-rotations",
        key=key,
    )

    return __utils.FreeChampionRotation(
        free_champion_ids=r["freeChampionIds"],
        free_champion_ids_for_new_players=r["freeChampionIdsForNewPlayers"],
        max_new_player_level=r["maxNewPlayerLevel"],
    )


def clash():
    pass


def league_challenger(key: str, region: region, queue: queue) -> object:
    """Get the challenger league for given queue.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        queue (enum): Queue enum.

    Returns:
        object: League object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue.value}",
        key=key,
    )

    return __utils.League(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=r["entries"],
    )


def league_by_summoner_id(key: str, region: region, summoner_id: str) -> list:
    """Get league entries in all queues for a given summoner ID.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        summoner_id (str): Summoner ID.

    Returns:
        list: List of LeagueEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}",
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


def league_by_queue_tier_division(
    key: str,
    region: region,
    queue: queue,
    tier: tier,
    division: division,
    page: int = 1,
) -> list:
    """Get all the league entries.

    Args:
        key (str): Riot API key.
        region (Enum): Region enum.
        queue (Enum): Queue enum.
        tier (Enum): Ranked tier enum.
        division (Enum): Ranked division enum.
        page (int): Page of entries to retrieve.

    Returns:
        list: List of LeagueEntry objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/league/v4/entries/{queue.value}/{tier.value}/{division.value}?page={page}",
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


def league_grandmaster(key: str, region: region, queue: queue) -> object:
    """Get the grandmaster league for given queue.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        queue (enum): Queue enum.

    Returns:
        object: League object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue.value}",
        key=key,
    )

    return __utils.League(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=r["entries"],
    )


def league_by_league_id(key: str, region: region, league_id: str) -> object:
    """Get league with given ID, including inactive entries.

    Args:
        key (str): Riot API key.
        region (Enum): Region enum.
        league_id (str): League ID.

    Returns:
        object: League object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/league/v4/leagues/{league_id}",
        key=key,
    )

    return __utils.League(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=r["entries"],
    )


def league_master(key: str, region: region, queue: queue) -> object:
    """Get the master league for given queue.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        queue (enum): Queue enum.

    Returns:
        object: League object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue.value}",
        key=key,
    )

    return __utils.League(
        tier=r["tier"],
        league_id=r["leagueId"],
        queue=r["queue"],
        name=r["name"],
        entries=r["entries"],
    )


def challenges_config(key: str, region: region) -> list:
    """List of all basic challenge configuration information (includes all translations for names and descriptions).

    Args:
        key (str): Riot API key.
        region (Enum): Region enum.

    Returns:
        list: List of ChallengeConfig objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/config",
        key=key,
    )

    for item in r:
        entry = __utils.ChallengeConfig(
            challenge_id=item["id"],
            leaderboard=item["leaderboard"],
            localized_names=item["localizedNames"],
            state=item["state"],
            thresholds=item["thresholds"],
        )

        entries.append(entry)

    return entries


def challenges_percentiles(key: str, region: region) -> dict:
    """Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it.

    Args:
        key (str): Riot API key.
        region (Enum): Region enum.

    Returns:
        dict: Percentiles dictionary.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/percentiles",
        key=key,
    )

    return r


def challenges_config_by_challenge_id(
    key: str, region: region, challenge_id: int
) -> object:
    """Get challenge configuration (REST).

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        challenge_id (int): Challenge ID.

    Returns:
        object: ChallengeConfig object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/config",
        key=key,
    )

    return __utils.ChallengeConfig(
        challenge_id=r["id"],
        leaderboard=r["leaderboard"],
        localized_names=r["localizedNames"],
        state=r["state"],
        thresholds=r["thresholds"],
    )


def challenges_apex_players(
    key: str, region: region, challenge_id: int, level: level
) -> list:
    """Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER.

    Args:
        key (str): Riot API key.
        region (Enum): Region enum.
        challenge_id (int): Challenge ID.
        level (Enum): Level enum.

    Returns:
        list: List of ApexPlayersInfo objects.
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level.value}",
        key=key,
    )

    for item in r:
        entry = __utils.ApexPlayersInfo(
            position=item["position"],
            puuid=item["puuid"],
            value=item["value"],
        )

        entries.append(entry)

    return entries


def challenges_percentiles_by_challenge_id(
    key: str, region: region, challenge_id: int
) -> object:
    """Map of level to percentile of players who have achieved it.

    Args:
        key (str): Riot API key.
        region (enum): Region enum.
        challenge_id (int): Challenge ID.

    Returns:
        object: Percentiles object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/percentiles",
        key=key,
    )

    return __utils.Percentiles(
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


def challenges(key: str, region: region, puuid: str) -> object:
    """Returns player information with list of all progressed challenges (REST).

    Args:
        key (str): Riot API key.
        region (Enum): Region enum.
        puuid (str): Puuid.

    Returns:
        object: PlayerInfo object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/player-data/{puuid}",
        key=key,
    )

    return __utils.PlayerInfo(
        category_points=r["categoryPoints"],
        challenges=r["challenges"],
        preferences=r["preferences"],
        total_points=r["totalPoints"],
    )


def status(key: str, region: region) -> object:
    """Get League of Legends status for the given platform.

    Args:
        key (str): Riot API key.
        region (Enum): Region enum.

    Returns:
        object: PlatformStatus object.
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/status/v4/platform-data",
        key=key,
    )

    return __utils.PlatformStatus(
        platform_id=r["id"],
        incidents=r["incidents"],
        locales=r["locales"],
        maintenances=r["maintenances"],
        name=r["name"],
    )


def match_history(
    key: str,
    continent: continent,
    puuid: str,
    queue: int,
    start: int = 0,
    count: int = 20,
) -> list:
    """Get a list of match ids by puuid.

    Args:
        key (str): Riot API key.
        continent (enum): Continent enum.
        puuid (str): Puuid.
        queue (int): Queue ID
        start (int, optional): Start index. Defaults to 0.
        count (int, optional): Valid values: 0 to 100. Number of match IDs to return. Defaults to 20.

    Returns:
        list: List of match IDs.
    """

    r = __utils.call(
        url=f"https://{continent.value}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue={queue}&start={start}&count={count}",
        key=key,
    )

    return r
