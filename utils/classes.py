from dataclasses import dataclass


@dataclass
class ChampionMastery:
    puuid: str
    champion_id: int
    champion_level: int
    champion_points: int
    last_play_time: int
    champion_points_since_last_level: int
    champion_points_until_next_level: int
    chest_granted: bool
    tokens_earned: int
    summoner_id: str


@dataclass
class ChampionInfo:
    free_champion_ids: list[int]
    free_champion_ids_for_new_players: list[int]
    max_new_player_level: int


@dataclass
class MiniSeries:
    losses: int
    progress: str
    target: int
    wins: int


@dataclass
class LeagueItem:
    summoner_id: str
    summoner_name: str
    mini_series: MiniSeries
    league_points: int
    rank: str
    wins: int
    losses: int
    veteran: bool
    inactive: bool
    fresh_blood: bool
    hot_streak: bool


@dataclass
class LeagueList:
    tier: str
    league_id: str
    queue: str
    name: str
    entries: list[LeagueItem]


@dataclass
class LeagueEntry:
    fresh_blood: bool
    hot_streak: bool
    inactive: bool
    league_id: str
    league_points: int
    losses: int
    mini_series: MiniSeries
    queue_type: str
    rank: str
    summoner_id: str
    summoner_name: str
    tier: str
    veteran: bool
    wins: int


@dataclass
class Thresholds:
    iron: int
    bronze: int
    silver: int
    gold: int
    platinum: int
    diamond: int
    master: int
    grandmaster: int
    challenger: int


@dataclass
class ChallengeConfigInfo:
    challenge_id: int
    leaderboard: bool
    localized_names: dict
    state: str
    thresholds: Thresholds
    tracking: str
    start_timestamp: int
    end_timestamp: int


@dataclass
class Percentiles:
    iron: int
    bronze: int
    silver: int
    gold: int
    platinum: int
    diamond: int
    master: int
    grandmaster: int
    challenger: int


@dataclass
class ApexPlayerInfo:
    position: int
    puuid: str
    value: int


@dataclass
class ChallengeInfo:
    achieved_time: int
    challenge_id: int
    level: str
    percentile: int
    value: int


@dataclass
class Collection:
    current: int
    level: str
    max: int
    percentile: int


@dataclass
class Expertise:
    current: int
    level: str
    max: int
    percentile: int


@dataclass
class Imagination:
    current: int
    level: str
    max: int
    percentile: int


@dataclass
class Teamwork:
    current: int
    level: str
    max: int
    percentile: int


@dataclass
class Veterancy:
    current: int
    level: str
    max: int
    percentile: int


@dataclass
class CategoryPoints:
    collection: Collection
    expertise: Expertise
    imagination: Imagination
    teamwork: Teamwork
    veterancy: Veterancy


@dataclass
class PlayerClientPreferences:
    banner_accent: str
    challenge_ids: list[int]
    crest_border: str
    prestige_crest_border_level: int
    title: str


@dataclass
class ChallengePoints:
    current: int
    level: str
    max: int
    percentile: int


@dataclass
class PlayerInfo:
    category_points: CategoryPoints
    challenges: list[ChallengeInfo]
    preferences: PlayerClientPreferences
    total_points: ChallengePoints


@dataclass
class Content:
    locale: str
    content: str


@dataclass
class Update:
    update_id: int
    author: str
    publish: bool
    publish_locations: list[str]
    translations: list[Content]
    created_at: str
    updated_at: str


@dataclass
class Status:
    status_id: int
    maintenance_status: str
    incident_severity: str
    titles: list[Content]
    updates: list[Update]
    created_at: str
    archive_at: str
    updated_at: str
    platforms: list[str]


@dataclass
class PlatformData:
    platform_id: str
    incidents: list[Status]
    locales: list[str]
    maintenances: list[Status]
    name: str


@dataclass
class Metadata:
    data_version: str
    match_id: str
    participants: list[str]


@dataclass
class PerkStats:
    defense: int
    flex: int
    offense: int


@dataclass
class PerkStyleSelection:
    perk: int
    var_1: int
    var_2: int
    var_3: int


@dataclass
class PerkStyle:
    description: str
    selections: list[PerkStyleSelection]
    style: int


@dataclass
class Perks:
    stat_perks: PerkStats
    styles: list[PerkStyle]


@dataclass
class Participant:
    assists: int
    baron_kills: int
    bounty_level: int
    champ_experience: int
    champ_level: int
    champion_id: int
    champion_name: str
    champion_transform: int
    consumables_purchased: int
    damage_dealt_to_buildings: int
    damage_dealt_to_objectives: int
    damage_dealt_to_turrets: int
    damage_self_mitigated: int
    deaths: int
    detector_wards_placed: int
    double_kills: int
    dragon_kills: int
    first_blood_assist: bool
    first_blood_kill: bool
    first_tower_assist: bool
    first_tower_kill: bool
    game_ended_in_early_surrender: bool
    game_ended_in_surrender: bool
    gold_earned: int
    gold_spent: int
    individual_position: str
    inhibitor_kills: int
    inhibitor_takedowns: int
    inhibitors_lost: int
    item_0: int
    item_1: int
    item_2: int
    item_3: int
    item_4: int
    item_5: int
    item_6: int
    items_purchased: int
    killing_sprees: int
    kills: int
    lane: str
    largest_critical_strike: int
    largest_killing_spree: int
    largest_multi_kill: int
    longest_time_spent_living: int
    magic_damage_dealt: int
    magic_damage_dealt_to_champions: int
    magic_damage_taken: int
    neutral_minions_killed: int
    nexus_kills: int
    nexus_takedowns: int
    nexus_lost: int
    objectives_stolen: int
    objectives_stolen_assists: int
    participant_id: int
    penta_kills: int
    perks: Perks
    physical_damage_dealt: int
    physical_damage_dealt_to_champions: int
    physical_damage_taken: int
    profile_icon: int
    puuid: str
    quadra_kills: int
    riot_id_name: str
    riot_id_tagline: str
    role: str
    sight_wards_bought_in_game: int
    spell_1_casts: int
    spell_2_casts: int
    spell_3_casts: int
    spell_4_casts: int
    summoner_1_casts: int
    summoner_1_id: int
    summoner_2_casts: int
    summoner_2_id: int
    summoner_id: str
    summoner_level: int
    summoner_name: str
    team_early_surrendered: bool
    team_id: int
    team_position: str
    time_ccing_others: int
    time_played: int
    total_damage_dealt: int
    total_damage_dealt_to_champions: int
    total_damage_shielded_on_teammates: int
    total_damage_taken: int
    total_heal: int
    total_heals_on_teammates: int
    total_minions_killed: int
    total_time_cc_dealt: int
    total_time_spent_dead: int
    total_units_healed: int
    triple_kills: int
    true_damage_dealt: int
    true_damage_dealt_to_champions: int
    true_damage_taken: int
    turret_kills: int
    turret_takedowns: int
    turrets_lost: int
    unreal_kills: int
    vision_score: int
    vision_wards_bought_in_game: int
    wards_killed: int
    wards_placed: int
    win: bool


@dataclass
class Ban:
    champion_id: int
    pick_turn: int


@dataclass
class Objective:
    first: bool
    kills: int


@dataclass
class Objectives:
    baron: Objective
    champion: Objective
    dragon: Objective
    inhibitor: Objective
    rift_herald: Objective
    tower: Objective


@dataclass
class Team:
    bans: list[Ban]
    objectives: Objectives
    team_id: int
    win: bool


@dataclass
class Info:
    game_creation: int
    game_duration: int
    game_end_timestamp: int
    game_id: int
    game_mode: str
    game_name: str
    game_start_timestamp: int
    game_type: str
    game_version: str
    map_id: int
    participants: list[Participant]
    platform_id: str
    queue_id: int
    teams: list[Team]
    tournament_code: str


@dataclass
class Match:
    info: Info
    metadata: Metadata


@dataclass
class TimelineParticipant:
    participant_id: int
    puuid: str


@dataclass
class TimelineInfo:
    frame_interval: int
    frames: list[dict]
    game_id: int
    participants: list[TimelineParticipant]


@dataclass
class TimelineMetadata:
    data_version: str
    match_id: int
    participants: list[str]


@dataclass
class MatchTimeline:
    info: TimelineInfo
    metadata: TimelineMetadata


@dataclass
class BannedChampion:
    pick_turn: int
    champion_id: int
    team_id: int


@dataclass
class Observer:
    encryption_key: str


@dataclass
class CurrentGamePeks:
    perk_ids: list[int]
    perk_style: int
    perk_sub_style: int


@dataclass
class GameCustomizationObject:
    category: str
    content: str


@dataclass
class CurrentGameParticipant:
    champion_id: int
    perks: CurrentGamePeks
    profile_icon_id: int
    bot: bool
    team_id: int
    summoner_name: str
    summoner_id: str
    spell_1_id: int
    spell_2_id: int
    game_customization_objects: list[GameCustomizationObject]


@dataclass
class CurrentGameInfo:
    banned_champions: list[BannedChampion]
    game_id: int
    length: int
    mode: str
    queue_config_id: int
    start_time: int
    game_type: str
    map_id: int
    observers: Observer
    participants: list[CurrentGameParticipant]
    platform_id: str


@dataclass
class FeaturedGameParticipant:
    bot: bool
    spell_2_id: int
    profile_icon_id: int
    summoner_name: str
    champion_id: int
    team_id: int
    spell_1_id: int


@dataclass
class FeaturedGameInfo:
    game_mode: str
    game_length: int
    map_id: int
    game_type: str
    banned_champions: list[BannedChampion]
    game_id: int
    observers: Observer
    game_queue_config_id: int
    game_start_time: int
    participants: list[FeaturedGameParticipant]
    platform_id: str


@dataclass
class FeaturedGames:
    client_refresh_interval: int
    game_list: list[FeaturedGameInfo]


@dataclass
class Summoner:
    account_id: str
    summoner_id: str
    name: str
    profile_icon_id: int
    puuid: str
    revision_date: int
    summoner_level: int
