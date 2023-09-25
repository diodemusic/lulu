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
    """Get account by puuid

    Args:
        key (str): Riot API key
        continent (enum): Continent enum
        puuid (str): Puuid

    Returns:
        object: Account object
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
    """Get account by riot id

    Args:
        key (str): Riot API key
        continent (enum): Continent enum
        game_name (str): In game name
        tag_line (str): In game tag line

    Returns:
        object: Account object
    """

    r = __utils.call(
        url=f"https://{continent.value}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}",
        key=key,
    )

    return __utils.Account(
        puuid=r["puuid"], game_name=r["gameName"], tag_line=r["tagLine"]
    )


def mastery_by_puuid(key: str, region: region, puuid: str) -> list:
    """Get all champion mastery entries sorted by number of champion points descending

    Args:
        region (enum): Region enum
        puuid (str): Puuid

    Returns:
        list: List of MasteryEntry objects
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}",
        key=key,
    )

    for item in r:
        entry = __utils.MasteryEntry(
            puuid=puuid,
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
    """Get all champion mastery entries sorted by number of champion points descending

    Args:
        region (enum): Region enum
        summoner_id (str): Summoner id

    Returns:
        list: List of MasteryEntry objects
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


def champion_free_rotation(key: str, region: region) -> object:
    """Returns champion rotations, including free-to-play and low-level free-to-play rotations

    Args:
        region (enum): Region enum

    Returns:
        object: FreeChampionRotation object
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
    """Get the challenger league for given queue

    Args:
        region (enum): Region enum
        queue (enum): Queue enum

    Returns:
        object: League object
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
    """Get league entries in all queues for a given summoner ID

    Args:
        region (enum): Region enum
        summoner_id (str): Summoner id

    Returns:
        list: List of LeagueEntry objects
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
    """Get all the league entries

    Args:
        region (Enum): Region enum
        queue (Enum): Queue enum
        tier (Enum): Ranked tier enum
        division (Enum): Ranked division enum
        page (int): Page of entries to retrieve

    Returns:
        list: List of LeagueEntry objects
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
    """Get the grandmaster league for given queue

    Args:
        region (enum): Region enum
        queue (enum): Queue enum

    Returns:
        object: League object
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
    """Get league with given ID, including inactive entries

    Args:
        region (Enum): Region enum
        league_id (str): League id

    Returns:
        object: League object
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
    """Get the master league for given queue

    Args:
        region (enum): Region enum
        queue (enum): Queue enum

    Returns:
        object: League object
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
    """List of all basic challenge configuration information (includes all translations for names and descriptions)

    Args:
        region (Enum): Region enum

    Returns:
        list: List of Config objects
    """

    entries = []

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/config",
        key=key,
    )

    for item in r:
        entry = __utils.Config(
            challenge_id=item["id"],
            leaderboard=item["leaderboard"],
            localized_names=item["localizedNames"],
            state=item["state"],
            thresholds=item["thresholds"],
        )

        entries.append(entry)

    return entries


def challenges_percentiles(key: str, region: region) -> dict:
    """Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it

    Args:
        region (Enum): Region enum

    Returns:
        dict: Percentiles dictionary
    """

    r = __utils.call(
        url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/percentiles",
        key=key,
    )

    return r


def challenges_apex_players(
    key: str, region: region, challenge_id: int, level: level
) -> list:
    """Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER

    Args:
        region (Enum): Region enum
        challenge_id (int): Challenge id
        level (Enum): Level enum

    Returns:
        list: List of ApexPlayersInfo objects
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


def challenges(key: str, region: region, puuid: str) -> object:
    """Returns player information with list of all progressed challenges (REST)

    Args:
        region (Enum): Region enum
        puuid (str): Puuid

    Returns:
        object: PlayerInfo object
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
        region (Enum): Region enum

    Returns:
        object: PlatformStatus object
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


def match_history(key: str, region: region, puuid: str):
    r = __utils.call(url=f"")

    return r
