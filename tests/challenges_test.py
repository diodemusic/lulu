import lulu
from dotenv import load_dotenv
import os
import utils


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw
puuid = os.getenv("PUUID")
challenge_id = 402400
level = lulu.level.master


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_config():
    instances = lulu.challenges.config(region)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.ChallengeConfigInfo
        assert type(instance.challenge_id) == int
        assert type(instance.leaderboard) == bool
        assert type(instance.localized_names) == dict

        for _, v in instance.localized_names.items():
            assert type(v["description"]) == str
            assert type(v["name"]) == str
            assert type(v["shortDescription"]) == str

        assert type(instance.state) == str
        assert type(instance.thresholds) == utils.classes.Thresholds
        assert type(instance.tracking) == str
        assert type(instance.start_timestamp) == int
        assert type(instance.end_timestamp) == int

        assert (
            type(instance.thresholds.iron) == float
            or type(instance.thresholds.iron) == int
        )
        assert (
            type(instance.thresholds.bronze) == float
            or type(instance.thresholds.bronze) == int
        )
        assert (
            type(instance.thresholds.silver) == float
            or type(instance.thresholds.silver) == int
        )
        assert (
            type(instance.thresholds.gold) == float
            or type(instance.thresholds.gold) == int
        )
        assert (
            type(instance.thresholds.platinum) == float
            or type(instance.thresholds.platinum) == int
        )
        assert (
            type(instance.thresholds.diamond) == float
            or type(instance.thresholds.diamond) == int
        )
        assert (
            type(instance.thresholds.master) == float
            or type(instance.thresholds.master) == int
        )
        assert (
            type(instance.thresholds.grandmaster) == float
            or type(instance.thresholds.grandmaster) == int
        )
        assert (
            type(instance.thresholds.challenger) == float
            or type(instance.thresholds.challenger) == int
        )


def test_percentiles():
    instances = lulu.challenges.percentiles(region)

    assert type(instances) == dict

    for _, v in instances.items():
        assert type(v) == utils.classes.Percentiles
        assert type(v.iron) == float
        assert type(v.bronze) == float
        assert type(v.silver) == float
        assert type(v.gold) == float
        assert type(v.platinum) == float
        assert type(v.diamond) == float
        assert type(v.master) == float
        assert type(v.grandmaster) == float
        assert type(v.challenger) == float


def test_config_by_challenge_id():
    instance = lulu.challenges.config_by_challenge_id(region, challenge_id)

    assert type(instance) == utils.classes.ChallengeConfigInfo
    assert type(instance.challenge_id) == int
    assert type(instance.leaderboard) == bool
    assert type(instance.localized_names) == dict

    for _, v in instance.localized_names.items():
        assert type(v["description"]) == str
        assert type(v["name"]) == str
        assert type(v["shortDescription"]) == str

    assert type(instance.state) == str
    assert type(instance.thresholds) == utils.classes.Thresholds
    assert type(instance.tracking) == str
    assert type(instance.start_timestamp) == int
    assert type(instance.end_timestamp) == int

    assert type(instance.thresholds.iron) == float
    assert type(instance.thresholds.bronze) == float
    assert type(instance.thresholds.silver) == float
    assert type(instance.thresholds.gold) == float
    assert type(instance.thresholds.diamond) == float
    assert type(instance.thresholds.master) == float
    assert type(instance.thresholds.grandmaster) == float
    assert type(instance.thresholds.challenger) == float


def test_apex_players():
    instances = lulu.challenges.apex_players(region, challenge_id, level)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.ApexPlayerInfo
        assert type(instance.position) == int
        assert type(instance.puuid) == str
        assert type(instance.value) == int


def test_percentiles_by_challenge_id():
    instance = lulu.challenges.percentiles_by_challenge_id(region, challenge_id)

    assert type(instance) == utils.classes.Percentiles
    assert type(instance.iron) == float
    assert type(instance.bronze) == float
    assert type(instance.silver) == float
    assert type(instance.gold) == float
    assert type(instance.platinum) == float
    assert type(instance.diamond) == float
    assert type(instance.master) == float
    assert type(instance.grandmaster) == float
    assert type(instance.challenger) == float


def test_by_puuid():
    instance = lulu.challenges.by_puuid(
        region,
        puuid,
    )

    assert type(instance) == utils.classes.PlayerInfo
    assert type(instance.challenges) == list
    assert type(instance.preferences) == utils.classes.PlayerClientPreferences
    assert type(instance.total_points) == utils.classes.ChallengePoints
    assert type(instance.category_points) == utils.classes.CategoryPoints

    for challenge in instance.challenges:
        assert type(challenge) == utils.classes.ChallengeInfo
        assert type(challenge.achieved_time) == int
        assert type(challenge.challenge_id) == int
        assert type(challenge.level) == str
        assert type(challenge.percentile) == float
        assert type(challenge.value) == float

    assert type(instance.preferences.banner_accent) == str
    assert type(instance.preferences.challenge_ids) == list

    for challenge_id in instance.preferences.challenge_ids:
        assert type(challenge_id) == int

    assert type(instance.preferences.crest_border) == str
    assert type(instance.preferences.prestige_crest_border_level) == int
    assert type(instance.preferences.title) == str

    assert type(instance.total_points.current) == int
    assert type(instance.total_points.level) == str
    assert type(instance.total_points.max) == int
    assert type(instance.total_points.percentile) == float

    assert type(instance.category_points.collection) == utils.classes.Collection
    assert type(instance.category_points.expertise) == utils.classes.Expertise
    assert type(instance.category_points.imagination) == utils.classes.Imagination
    assert type(instance.category_points.teamwork) == utils.classes.Teamwork
    assert type(instance.category_points.veterancy) == utils.classes.Veterancy

    assert type(instance.category_points.collection.current) == int
    assert type(instance.category_points.collection.level) == str
    assert type(instance.category_points.collection.max) == int
    assert type(instance.category_points.collection.max) == int

    assert type(instance.category_points.expertise.current) == int
    assert type(instance.category_points.expertise.level) == str
    assert type(instance.category_points.expertise.max) == int
    assert type(instance.category_points.expertise.max) == int

    assert type(instance.category_points.imagination.current) == int
    assert type(instance.category_points.imagination.level) == str
    assert type(instance.category_points.imagination.max) == int
    assert type(instance.category_points.imagination.max) == int

    assert type(instance.category_points.teamwork.current) == int
    assert type(instance.category_points.teamwork.level) == str
    assert type(instance.category_points.teamwork.max) == int
    assert type(instance.category_points.teamwork.max) == int

    assert type(instance.category_points.veterancy.current) == int
    assert type(instance.category_points.veterancy.level) == str
    assert type(instance.category_points.veterancy.max) == int
    assert type(instance.category_points.veterancy.max) == int
