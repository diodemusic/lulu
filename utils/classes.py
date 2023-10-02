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


class ChallengeConfig:
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


class Percentiles:
    def __init__(
        self,
        iron,
        bronze,
        silver,
        gold,
        platinum,
        diamond,
        master,
        grandmaster,
        challenger,
        none,
    ):
        self.iron = iron
        self.bronze = bronze
        self.silver = silver
        self.gold = gold
        self.platinum = platinum
        self.diamond = diamond
        self.master = master
        self.grandmaster = grandmaster
        self.challenger = challenger
        self.none = none


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


class MatchInfo:
    def __init__(
        self,
        creation,
        duration,
        end_timestamp,
        game_id,
        mode,
        name,
        start_timestamp,
        game_type,
        version,
        map_id,
        participants,
        platform_id,
        queue_id,
        teams,
        tournament_code,
    ):
        self.creation = creation
        self.duration = duration
        self.end_timestamp = end_timestamp
        self.game_id = game_id
        self.mode = mode
        self.name = name
        self.start_timestamp = start_timestamp
        self.game_type = game_type
        self.version = version
        self.map_id = map_id
        self.participants = participants
        self.platform_id = platform_id
        self.queue_id = queue_id
        self.teams = teams
        self.tournament_code = tournament_code


class Metadata:
    def __init__(self, data_version, match_id, participants):
        self.data_version = data_version
        self.match_id = match_id
        self.participants = participants


class Match:
    def __init__(self, info, metadata):
        self.info = info
        self.metadata = metadata


class TimelineInfo:
    def __init__(self, frame_interval, frames, game_id, participants):
        self.frame_interval = frame_interval
        self.frames = frames
        self.game_id = game_id
        self.participants = participants


class MatchTimeline:
    def __init__(self, info, metadata):
        self.info = info
        self.metadata = metadata


class Spectator:
    def __init__(
        self,
        banned_champions,
        game_id,
        length,
        mode,
        queue_config_id,
        start_time,
        game_type,
        map_id,
        observers,
        participants,
        platform_id,
    ):
        self.banned_champions = banned_champions
        self.game_id = game_id
        self.length = length
        self.mode = mode
        self.queue_config_id = queue_config_id
        self.start_time = start_time
        self.game_type = game_type
        self.map_id = map_id
        self.observers = observers
        self.participants = participants
        self.platform_id = platform_id


class FeaturedGames:
    def __init__(self, client_refresh_interval, game_list):
        self.client_refresh_interval = client_refresh_interval
        self.game_list = game_list


class Summoner:
    def __init__(
        self,
        account_id,
        summoner_id,
        name,
        profile_icon_id,
        puuid,
        revision_date,
        level,
    ):
        self.account_id = account_id
        self.summoner_id = summoner_id
        self.name = name
        self.profile_icon_id = profile_icon_id
        self.puuid = puuid
        self.revision_date = revision_date
        self.level = level
