import os
import pickle
import time
import logging
import requests


cache_dir = "cache"
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)


def save_to_cache(cache_data, cache_key: str):
    cache_path = os.path.join(cache_dir, f"{cache_key}.pkl")
    cache_data = {"data": cache_data, "timestamp": int(time.time())}

    with open(cache_path, "wb") as cfp:
        pickle.dump(cache_data, cfp)


def load_from_cache(cache_key: str, ttl: int):
    cache_path = os.path.join(cache_dir, f"{cache_key}.pkl")

    if os.path.exists(cache_path):
        with open(cache_path, "rb") as cfp:
            cache_data = pickle.load(cfp)

            if int(time.time()) - cache_data["timestamp"] <= ttl:
                return cache_data["data"]

    return None


def call(key: str, url: str, max_retries: int = 3, retry_delay: int = 40):
    cache_key = (
        url.split("https://")[1].replace(".", "_").replace("/", "_").replace("?", "_")
    )

    cached_response = load_from_cache(cache_key=cache_key, ttl=3600)

    if cached_response is not None:
        return cached_response

    headers = {"X-Riot-Token": key}

    for retry in range(max_retries + 1):
        logging.info(url)

        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            r_dict = r.json()

            save_to_cache(cache_data=r_dict, cache_key=cache_key)

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


class Account:
    def __init__(self, puuid: str, game_name: str, tag_line: str):
        self.puuid = puuid
        self.game_name = game_name
        self.tag_line = tag_line


class MasteryEntry:
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


class FreeChampionRotation:
    def __init__(
        self, free_champion_ids, free_champion_ids_for_new_players, max_new_player_level
    ):
        self.free_champion_ids = free_champion_ids
        self.free_champion_ids_for_new_players = free_champion_ids_for_new_players
        self.max_new_player_level = max_new_player_level


class Entry:
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


class League:
    def __init__(self, tier, league_id, queue, name, entries):
        self.tier = tier
        self.league_id = league_id
        self.queue = queue
        self.name = name
        self.entries = [Entry(**entry_data) for entry_data in entries]


class LeagueEntry:
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


class Config:
    def __init__(self, challenge_id, leaderboard, localized_names, state, thresholds):
        self.challenge_id = challenge_id
        self.leaderboard = leaderboard
        self.localized_names = localized_names
        self.state = state
        self.thresholds = thresholds


class ApexPlayersInfo:
    def __init__(self, position, puuid, value):
        self.position = position
        self.puuid = puuid
        self.value = value


class PlayerInfo:
    def __init__(self, category_points, challenges, preferences, total_points):
        self.category_points = category_points
        self.challenges = challenges
        self.preferences = preferences
        self.total_points = total_points


class PlatformStatus:
    def __init__(self, platform_id, incidents, locales, maintenances, name):
        self.platform_id = platform_id
        self.incidents = incidents
        self.locales = locales
        self.maintenances = maintenances
        self.name = name


class MatchHistory:
    def __init__(
        self,
    ):
        pass
