import requests
import time
import logging
from enum import Enum
import os
import pickle


logging.basicConfig(
    level=logging.INFO,  # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


_cache_dir = "cache"

if not os.path.exists(_cache_dir):
    os.makedirs(_cache_dir)


def _save_to_cache(cache_data, cache_key: str):
    cache_path = os.path.join(_cache_dir, f"{cache_key}.pkl")
    cache_data = {"data": cache_data, "timestamp": int(time.time())}

    with open(cache_path, "wb") as cfp:
        pickle.dump(cache_data, cfp)


def _load_from_cache(cache_key: str, ttl: int):
    cache_path = os.path.join(_cache_dir, f"{cache_key}.pkl")

    if os.path.exists(cache_path):
        with open(cache_path, "rb") as cfp:
            cache_data = pickle.load(cfp)

            if int(time.time()) - cache_data["timestamp"] <= ttl:
                return cache_data["data"]

    return None


class Continent(Enum):
    americas = "americas"
    asia = "asia"
    esports = "esports"
    europe = "europe"


class Region(Enum):
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


class Queue(Enum):
    solo_duo = "RANKED_SOLO_5x5"
    flex = "RANKED_FLEX_SR"


class Tier(Enum):
    iron = "IRON"
    bronze = "BRONZE"
    silver = "SILVER"
    gold = "GOLD"
    platinum = "PLATINUM"
    emerald = "EMERALD"
    diamond = "DIAMOND"


class Division(Enum):
    one = "I"
    two = "II"
    three = "III"
    four = "IV"


class ChallengesLevel(Enum):
    master = "MASTER"
    grandmaster = "GRANDMASTER"
    challenger = "CHALLENGER"


class ApiConfig:
    def __init__(self, api_key: str):
        self.api_key = api_key


class SetKey:
    def __init__(self, api_key: str):
        self.api_config = ApiConfig(api_key)
        self.account = Account(self.api_config)
        self.champion_mastery = ChampionMastery(self.api_config)
        self.champion = Champion(self.api_config)
        self.clash = Clash(self.api_config)
        self.league = League(self.api_config)
        self.challenges = Challenges(self.api_config)


class Lulu:
    def __init__(self, api_config: ApiConfig):
        self.api_config = api_config

    def _call(self, url: str, max_retries: int = 3, retry_delay: int = 40):
        cache_key = (
            url.split("https://")[1]
            .replace(".", "_")
            .replace("/", "_")
            .replace("?", "_")
        )

        cached_response = _load_from_cache(cache_key=cache_key, ttl=3600)

        if cached_response is not None:
            return cached_response

        headers = {"X-Riot-Token": self.api_config.api_key}

        for retry in range(max_retries + 1):
            logging.info(url)

            r = requests.get(url, headers=headers)

            if r.status_code == 200:
                r_dict = r.json()

                _save_to_cache(cache_data=r_dict, cache_key=cache_key)

                return r_dict

            elif r.status_code == 429:
                logging.warning(
                    f"Rate limited, Waiting {int(r.headers.get('Retry-After'))} seconds..."
                )

                time.sleep(int(r.headers.get("Retry-After")))

            else:
                logging.error(f"Status code >> {r.status_code}.")

                if retry < max_retries:
                    logging.info(f"Retrying in {retry_delay} seconds...")

                    time.sleep(retry_delay)

                else:
                    raise Exception("Max retries reached, giving up.")


class _Account:
    def __init__(self, puuid: str, game_name: str, tag_line: str):
        self.puuid = puuid
        self.game_name = game_name
        self.tag_line = tag_line


class Account(Lulu):
    def by_puuid(self, continent: Continent, puuid: str):
        """Get account by puuid

        Args:
            continent (enum): Continent enum
            puuid (str): Puuid

        Returns:
            class: Account class
        """

        r = self._call(
            url=f"https://{continent.value}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}",
        )

        return _Account(
            puuid=r["puuid"], game_name=r["gameName"], tag_line=r["tagLine"]
        )

    def by_riot_id(self, continent: Continent, game_name: str, tag_line: str):
        """Get account by riot id

        Args:
            continent (enum): Continent enum
            game_name (str): In game name
            tag_line (str): In game tag line

        Returns:
            class: Account class
        """

        r = self._call(
            url=f"https://{continent.value}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}",
        )

        return _Account(
            puuid=r["puuid"], game_name=r["gameName"], tag_line=r["tagLine"]
        )


class _MasteryEntry:
    def __init__(
        self,
        puuid,
        champion_id,
        level,
        points,
        last_play_time,
        points_since_last_level,
        points_until_next_level,
        chest_granted,
        tokens_earned,
        summoner_id,
    ):
        self.champion_id = champion_id
        self.puuid = puuid
        self.level = level
        self.points = points
        self.last_play_time = last_play_time
        self.points_since_last_level = points_since_last_level
        self.points_until_next_level = points_until_next_level
        self.chest_granted = chest_granted
        self.tokens_earned = tokens_earned
        self.summoner_id = summoner_id


class ChampionMastery(Lulu):
    def by_puuid(self, region: Region, puuid: str):
        """Get all champion mastery entries sorted by number of champion points descending

        Args:
            region (enum): Region enum
            puuid (str): Puuid

        Returns:
            list: List of MasteryEntry classes
        """

        entries = []

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}",
        )

        for item in r:
            entry = _MasteryEntry(
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

    def by_summoner_id(self, region: Region, summoner_id: str):
        """Get all champion mastery entries sorted by number of champion points descending

        Args:
            region (enum): Region enum
            summoner_id (str): Summoner id

        Returns:
            list: List of MasteryEntry classes
        """

        entries = []

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}",
        )

        for item in r:
            entry = _MasteryEntry(
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


class _FreeChampionRotation:
    def __init__(
        self, free_champion_ids, free_champion_ids_for_new_players, max_new_player_level
    ):
        self.free_champion_ids = free_champion_ids
        self.free_champion_ids_for_new_players = free_champion_ids_for_new_players
        self.max_new_player_level = max_new_player_level


class Champion(Lulu):
    def free_rotation(self, region: Region):
        """Returns champion rotations, including free-to-play and low-level free-to-play rotations

        Args:
            region (enum): Region enum

        Returns:
            class: FreeChampionRotation class
        """

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/platform/v3/champion-rotations",
        )

        return _FreeChampionRotation(
            free_champion_ids=r["freeChampionIds"],
            free_champion_ids_for_new_players=r["freeChampionIdsForNewPlayers"],
            max_new_player_level=r["maxNewPlayerLevel"],
        )


class Clash(Lulu):
    pass


class _Entry:
    def __init__(
        self,
        summonerId,
        summonerName,
        leaguePoints,
        rank,
        wins,
        losses,
        veteran,
        inactive,
        freshBlood,
        hotStreak,
    ):
        self.summoner_id = summonerId
        self.summoner_name = summonerName
        self.league_points = leaguePoints
        self.rank = rank
        self.wins = wins
        self.losses = losses
        self.veteran = veteran
        self.inactive = inactive
        self.fresh_blood = freshBlood
        self.hot_streak = hotStreak


class _League:
    def __init__(self, tier, league_id, queue, name, entries):
        self.tier = tier
        self.league_id = league_id
        self.queue = queue
        self.name = name
        self.entries = [_Entry(**entry_data) for entry_data in entries]


class _LeagueEntry:
    def __init__(
        self,
        fresh_blood,
        hot_streak,
        inactive,
        league_id,
        points,
        losses,
        queue_type,
        rank,
        summoner_id,
        summoner_name,
        tier,
        veteran,
        wins,
    ):
        self.fresh_blood = fresh_blood
        self.hot_streak = hot_streak
        self.inactive = inactive
        self.league_id = league_id
        self.points = points
        self.losses = losses
        self.queue_type = queue_type
        self.rank = rank
        self.summoner_id = summoner_id
        self.summoner_name = summoner_name
        self.tier = tier
        self.veteran = veteran
        self.wins = wins


class League(Lulu):
    def challenger(self, region: Region, queue: Queue):
        """Get the challenger league for given queue

        Args:
            region (enum): Region enum
            queue (enum): Queue enum

        Returns:
            class: League class
        """

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue.value}"
        )

        return _League(
            tier=r["tier"],
            league_id=r["leagueId"],
            queue=r["queue"],
            name=r["name"],
            entries=r["entries"],
        )

    def by_summoner_id(self, region: Region, summoner_id: str):
        """Get league entries in all queues for a given summoner ID

        Args:
            region (enum): Region enum
            summoner_id (str): Summoner id

        Returns:
            list: List of LeagueEntry classes
        """

        entries = []

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
        )

        for item in r:
            entry = _LeagueEntry(
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
        self,
        region: Region,
        queue: Queue,
        tier: Tier,
        division: Division,
        page: int = 1,
    ):
        """Get all the league entries

        Args:
            region (Enum): Region enum
            queue (Enum): Queue enum
            tier (Enum): Ranked tier enum
            division (Enum): Ranked division enum
            page (int): Page of entries to retrieve

        Returns:
            list: List of LeagueEntry classes
        """

        entries = []

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/league/v4/entries/{queue.value}/{tier.value}/{division.value}?page={page}"
        )

        for item in r:
            entry = _LeagueEntry(
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

    def grandmaster(self, region: Region, queue: Queue):
        """Get the grandmaster league for given queue

        Args:
            region (enum): Region enum
            queue (enum): Queue enum

        Returns:
            class: League class
        """

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue.value}"
        )

        return _League(
            tier=r["tier"],
            league_id=r["leagueId"],
            queue=r["queue"],
            name=r["name"],
            entries=r["entries"],
        )

    def by_league_id(self, region: Region, league_id: str):
        """Get league with given ID, including inactive entries

        Args:
            region (Enum): Region enum
            league_id (str): League id

        Returns:
            class: League class
        """

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/league/v4/leagues/{league_id}"
        )

        return _League(
            tier=r["tier"],
            league_id=r["leagueId"],
            queue=r["queue"],
            name=r["name"],
            entries=r["entries"],
        )

    def master(self, region: Region, queue: Queue):
        """Get the master league for given queue

        Args:
            region (enum): Region enum
            queue (enum): Queue enum

        Returns:
            class: League class
        """

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue.value}"
        )

        return _League(
            tier=r["tier"],
            league_id=r["leagueId"],
            queue=r["queue"],
            name=r["name"],
            entries=r["entries"],
        )


class _Config:
    def __init__(self, challenge_id, leaderboard, localized_names, state, thresholds):
        self.challenge_id = challenge_id
        self.leaderboard = leaderboard
        self.localized_names = localized_names
        self.state = state
        self.thresholds = thresholds


class _ApexPlayersInfo:
    def __init__(self, position, puuid, value):
        self.position = position
        self.puuid = puuid
        self.value = value


class _PlayerInfo:
    def __init__(self, category_points, challenges, preferences, total_points):
        self.category_points = category_points
        self.challenges = challenges
        self.preferences = preferences
        self.total_points = total_points


class Challenges(Lulu):
    def config(self, region: Region):
        """List of all basic challenge configuration information (includes all translations for names and descriptions)

        Args:
            region (Enum): Region enum

        Returns:
            list: List of Config classes
        """

        entries = []

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/config"
        )

        for item in r:
            entry = _Config(
                challenge_id=item["id"],
                leaderboard=item["leaderboard"],
                localized_names=item["localizedNames"],
                state=item["state"],
                thresholds=item["thresholds"],
            )

            entries.append(entry)

        return entries

    def percentiles(self, region: Region):
        """Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it

        Args:
            region (Enum): Region enum

        Returns:
            dict: dictionary
        """

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/percentiles"
        )

        return r

    def apex_players(self, region: Region, challenge_id: int, level: ChallengesLevel):
        """Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER

        Args:
            region (Enum): Region enum
            challenge_id (int): Challenge id
            level (Enum): Challenges level enum

        Returns:
            list: List of ApexPlayersInfo classes
        """

        entries = []

        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level.value}"
        )

        for item in r:
            entry = _ApexPlayersInfo(
                position=item["position"],
                puuid=item["puuid"],
                value=item["value"],
            )

            entries.append(entry)

        return entries

    def by_puuid(self, region: Region, puuid: str):
        """Returns player information with list of all progressed challenges (REST)

        Args:
            region (Enum): Region enum
            puuid (str): Puuid

        Returns:
            class: PlayerInfo class
        """
        r = self._call(
            url=f"https://{region.value}.api.riotgames.com/lol/challenges/v1/player-data/{puuid}"
        )

        return _PlayerInfo(
            category_points=r["categoryPoints"],
            challenges=r["challenges"],
            preferences=r["preferences"],
            total_points=r["totalPoints"],
        )
