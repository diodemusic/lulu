import lulu
from dotenv import load_dotenv
import os
import utils


load_dotenv()
key = os.getenv("KEY")
puuid = os.getenv("PUUID")
continent = lulu.continent.europe
queue = 400
match_id = lulu.match.history(continent, puuid, queue, 1)[0]


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_history():
    count = 10
    start = 3
    instance = lulu.match.history(continent, puuid, queue, start, count)

    assert type(instance) == list
    assert len(instance) == count

    for match_id in instance:
        assert type(match_id) == str


def test_by_match_id():
    instance = lulu.match.by_match_id(continent, match_id)

    assert type(instance.info) == utils.classes.Info
    assert type(instance.metadata) == utils.classes.Metadata

    assert type(instance.metadata.data_version) == str
    assert type(instance.metadata.match_id) == str
    assert type(instance.metadata.participants) == list

    for metadata_participant in instance.metadata.participants:
        assert type(metadata_participant) == str

    assert type(instance.info.game_creation) == int
    assert type(instance.info.game_duration) == int
    assert type(instance.info.game_end_timestamp) == int
    assert type(instance.info.game_id) == int
    assert type(instance.info.game_mode) == str
    assert type(instance.info.game_name) == str
    assert type(instance.info.game_start_timestamp) == int
    assert type(instance.info.game_type) == str
    assert type(instance.info.game_version) == str
    assert type(instance.info.map_id) == int
    assert type(instance.info.participants) == list

    for participant in instance.info.participants:
        assert type(participant) == utils.classes.Participant
        assert type(participant.assists) == int
        assert type(participant.baron_kills) == int
        assert type(participant.bounty_level) == int
        assert type(participant.champ_experience) == int
        assert type(participant.champ_level) == int
        assert type(participant.champion_id) == int
        assert type(participant.champion_name) == str
        assert type(participant.champion_transform) == int
        assert type(participant.consumables_purchased) == int
        assert type(participant.damage_dealt_to_buildings) == int
        assert type(participant.damage_dealt_to_objectives) == int
        assert type(participant.damage_dealt_to_turrets) == int
        assert type(participant.damage_self_mitigated) == int
        assert type(participant.deaths) == int
        assert type(participant.detector_wards_placed) == int
        assert type(participant.double_kills) == int
        assert type(participant.dragon_kills) == int
        assert type(participant.first_blood_assist) == bool
        assert type(participant.first_blood_kill) == bool
        assert type(participant.first_tower_assist) == bool
        assert type(participant.first_tower_kill) == bool
        assert type(participant.game_ended_in_early_surrender) == bool
        assert type(participant.game_ended_in_surrender) == bool
        assert type(participant.gold_earned) == int
        assert type(participant.gold_spent) == int
        assert type(participant.individual_position) == str
        assert type(participant.inhibitor_kills) == int
        assert type(participant.inhibitor_takedowns) == int
        assert type(participant.inhibitors_lost) == int
        assert type(participant.item_0) == int
        assert type(participant.item_1) == int
        assert type(participant.item_2) == int
        assert type(participant.item_3) == int
        assert type(participant.item_4) == int
        assert type(participant.item_5) == int
        assert type(participant.item_6) == int
        assert type(participant.items_purchased) == int
        assert type(participant.killing_sprees) == int
        assert type(participant.kills) == int
        assert type(participant.lane) == str
        assert type(participant.largest_critical_strike) == int
        assert type(participant.largest_killing_spree) == int
        assert type(participant.largest_multi_kill) == int
        assert type(participant.longest_time_spent_living) == int
        assert type(participant.magic_damage_dealt) == int
        assert type(participant.magic_damage_dealt_to_champions) == int
        assert type(participant.magic_damage_taken) == int
        assert type(participant.neutral_minions_killed) == int
        assert type(participant.nexus_kills) == int
        assert type(participant.nexus_takedowns) == int
        assert type(participant.nexus_lost) == int
        assert type(participant.objectives_stolen) == int
        assert type(participant.objectives_stolen_assists) == int
        assert type(participant.participant_id) == int
        assert type(participant.penta_kills) == int
        assert type(participant.perks) == utils.classes.Perks

        assert type(participant.perks.stat_perks) == utils.classes.PerkStats

        assert type(participant.perks.stat_perks.defense) == int
        assert type(participant.perks.stat_perks.flex) == int
        assert type(participant.perks.stat_perks.offense) == int

        assert type(participant.perks.styles) == list

        for style in participant.perks.styles:
            assert type(style) == utils.classes.PerkStyle
            assert type(style.description) == str
            assert type(style.selections) == list

            for selection in style.selections:
                assert type(selection) == utils.classes.PerkStyleSelection
                assert type(selection.perk) == int
                assert type(selection.var_1) == int
                assert type(selection.var_2) == int
                assert type(selection.var_3) == int

            assert type(style.style) == int

        assert type(participant.physical_damage_dealt) == int
        assert type(participant.physical_damage_dealt_to_champions) == int
        assert type(participant.physical_damage_taken) == int
        assert type(participant.profile_icon) == int
        assert type(participant.puuid) == str
        assert type(participant.quadra_kills) == int
        assert type(participant.riot_id_name) == str
        assert type(participant.riot_id_tagline) == str
        assert type(participant.role) == str
        assert type(participant.sight_wards_bought_in_game) == int
        assert type(participant.spell_1_casts) == int
        assert type(participant.spell_2_casts) == int
        assert type(participant.spell_3_casts) == int
        assert type(participant.spell_4_casts) == int
        assert type(participant.summoner_1_casts) == int
        assert type(participant.summoner_1_id) == int
        assert type(participant.summoner_2_casts) == int
        assert type(participant.summoner_2_id) == int
        assert type(participant.summoner_id) == str
        assert type(participant.summoner_level) == int
        assert type(participant.summoner_name) == str
        assert type(participant.team_early_surrendered) == bool
        assert type(participant.team_id) == int
        assert type(participant.team_position) == str
        assert type(participant.time_ccing_others) == int
        assert type(participant.time_played) == int
        assert type(participant.total_damage_dealt) == int
        assert type(participant.total_damage_dealt_to_champions) == int
        assert type(participant.total_damage_shielded_on_teammates) == int
        assert type(participant.total_damage_taken) == int
        assert type(participant.total_heal) == int
        assert type(participant.total_heals_on_teammates) == int
        assert type(participant.total_minions_killed) == int
        assert type(participant.total_time_cc_dealt) == int
        assert type(participant.total_time_spent_dead) == int
        assert type(participant.total_units_healed) == int
        assert type(participant.triple_kills) == int
        assert type(participant.true_damage_dealt) == int
        assert type(participant.true_damage_dealt_to_champions) == int
        assert type(participant.true_damage_taken) == int
        assert type(participant.turret_kills) == int
        assert type(participant.turret_takedowns) == int
        assert type(participant.turrets_lost) == int
        assert type(participant.unreal_kills) == int
        assert type(participant.vision_score) == int
        assert type(participant.vision_wards_bought_in_game) == int
        assert type(participant.wards_killed) == int
        assert type(participant.wards_placed) == int
        assert type(participant.win) == bool

    assert type(instance.info.platform_id) == str
    assert type(instance.info.queue_id) == int
    assert type(instance.info.teams) == list

    for team in instance.info.teams:
        assert type(team) == utils.classes.Team
        assert type(team.bans) == list

        for ban in team.bans:
            assert type(ban) == utils.classes.Ban
            assert type(ban.champion_id) == int
            assert type(ban.pick_turn) == int

        assert type(team.objectives) == utils.classes.Objectives
        assert type(team.objectives.baron.first) == bool
        assert type(team.objectives.baron.kills) == int

        assert type(team.objectives.champion) == utils.classes.Objective
        assert type(team.objectives.champion.first) == bool
        assert type(team.objectives.champion.kills) == int

        assert type(team.objectives.dragon) == utils.classes.Objective
        assert type(team.objectives.dragon.first) == bool
        assert type(team.objectives.dragon.kills) == int

        assert type(team.objectives.inhibitor) == utils.classes.Objective
        assert type(team.objectives.inhibitor.first) == bool
        assert type(team.objectives.inhibitor.kills) == int

        assert type(team.objectives.rift_herald) == utils.classes.Objective
        assert type(team.objectives.rift_herald.first) == bool
        assert type(team.objectives.rift_herald.kills) == int

        assert type(team.objectives.tower) == utils.classes.Objective
        assert type(team.objectives.tower.first) == bool
        assert type(team.objectives.tower.kills) == int

        assert type(team.team_id) == int
        assert type(team.win) == bool

    assert type(instance.info.tournament_code) == str


def test_timeline_by_match_id():
    timeline_by_match_id = lulu.match.timeline_by_match_id(continent, match_id)

    info = timeline_by_match_id.info
    metadata = timeline_by_match_id.metadata

    assert type(info.frame_interval) == int
    assert type(info.frames) == list

    for frame in info.frames:
        assert type(frame) == dict

    assert type(info.game_id) == int
    assert type(info.participants) == list

    for participant in info.participants:
        assert type(participant) == dict

    assert type(metadata.data_version) == str
    assert metadata.match_id == match_id
    assert type(metadata.participants) == list
