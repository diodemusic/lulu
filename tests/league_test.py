import lulu
from dotenv import load_dotenv
import os
import utils


load_dotenv()
key = os.getenv("KEY")
summoner_id = os.getenv("SUMMONER_ID")
league_id = os.getenv("LEAGUE_ID")
region = lulu.region.euw
queue = lulu.queue.solo_duo
tier = lulu.tier.gold
division = lulu.division.two


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_challenger_leagues_by_queue():
    instance = lulu.league.challenger_leagues_by_queue(region, queue)

    assert type(instance) == utils.classes.LeagueList
    assert type(instance.name) == str
    assert type(instance.entries) == list
    assert type(instance.league_id) == str
    assert type(instance.queue) == str
    assert type(instance.tier) == str

    for entry in instance.entries:
        assert type(entry) == utils.classes.LeagueItem
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_points) == int
        assert type(entry.losses) == int
        assert type(entry.rank) == str
        assert type(entry.summoner_id) == str
        assert type(entry.summoner_name) == str
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int
        assert type(entry.mini_series) == utils.classes.MiniSeries

        assert type(entry.mini_series.losses) == int
        assert type(entry.mini_series.progress) == str
        assert type(entry.mini_series.target) == int
        assert type(entry.mini_series.wins) == int


def test_by_summoner():
    instances = lulu.league.by_summoner(region, summoner_id)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.LeagueEntry
        assert type(instance.fresh_blood) == bool
        assert type(instance.hot_streak) == bool
        assert type(instance.inactive) == bool
        assert type(instance.league_id) == str
        assert type(instance.league_points) == int
        assert type(instance.losses) == int
        assert type(instance.queue_type) == str
        assert type(instance.rank) == str
        assert type(instance.summoner_id) == str
        assert type(instance.summoner_name) == str
        assert type(instance.tier) == str
        assert type(instance.veteran) == bool
        assert type(instance.wins) == int
        assert type(instance.mini_series) == utils.classes.MiniSeries

        assert type(instance.mini_series.losses) == int
        assert type(instance.mini_series.progress) == str
        assert type(instance.mini_series.target) == int
        assert type(instance.mini_series.wins) == int


def test_by_queue_tier_division():
    instances = lulu.league.by_queue_tier_division(
        region,
        queue,
        tier,
        division,
    )

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.LeagueEntry
        assert type(instance.fresh_blood) == bool
        assert type(instance.hot_streak) == bool
        assert type(instance.inactive) == bool
        assert type(instance.league_id) == str
        assert type(instance.league_points) == int
        assert type(instance.losses) == int
        assert type(instance.queue_type) == str
        assert type(instance.rank) == str
        assert type(instance.summoner_id) == str
        assert type(instance.summoner_name) == str
        assert type(instance.tier) == str
        assert type(instance.veteran) == bool
        assert type(instance.wins) == int
        assert type(instance.mini_series) == utils.classes.MiniSeries

        assert type(instance.mini_series.losses) == int
        assert type(instance.mini_series.progress) == str
        assert type(instance.mini_series.target) == int
        assert type(instance.mini_series.wins) == int


def test_grandmaster_leagues_by_queue():
    instance = lulu.league.grandmaster_leagues_by_queue(region, queue)

    assert type(instance) == utils.classes.LeagueList
    assert type(instance.name) == str
    assert type(instance.entries) == list
    assert type(instance.league_id) == str
    assert type(instance.queue) == str
    assert type(instance.tier) == str

    for entry in instance.entries:
        assert type(entry) == utils.classes.LeagueItem
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_points) == int
        assert type(entry.losses) == int
        assert type(entry.rank) == str
        assert type(entry.summoner_id) == str
        assert type(entry.summoner_name) == str
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int
        assert type(entry.mini_series) == utils.classes.MiniSeries

        assert type(entry.mini_series.losses) == int
        assert type(entry.mini_series.progress) == str
        assert type(entry.mini_series.target) == int
        assert type(entry.mini_series.wins) == int


def test_by_league_id():
    instance = lulu.league.by_league_id(region, league_id)

    assert type(instance) == utils.classes.LeagueList
    assert type(instance.name) == str
    assert type(instance.entries) == list
    assert type(instance.league_id) == str
    assert type(instance.queue) == str
    assert type(instance.tier) == str

    for entry in instance.entries:
        assert type(entry) == utils.classes.LeagueItem
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_points) == int
        assert type(entry.losses) == int
        assert type(entry.rank) == str
        assert type(entry.summoner_id) == str
        assert type(entry.summoner_name) == str
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int
        assert type(entry.mini_series) == utils.classes.MiniSeries

        assert type(entry.mini_series.losses) == int
        assert type(entry.mini_series.progress) == str
        assert type(entry.mini_series.target) == int
        assert type(entry.mini_series.wins) == int


def test_master_leagues_by_queue():
    instance = lulu.league.master_leagues_by_queue(region, queue)

    assert type(instance) == utils.classes.LeagueList
    assert type(instance.name) == str
    assert type(instance.entries) == list
    assert type(instance.league_id) == str
    assert type(instance.queue) == str
    assert type(instance.tier) == str

    for entry in instance.entries:
        assert type(entry) == utils.classes.LeagueItem
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_points) == int
        assert type(entry.losses) == int
        assert type(entry.rank) == str
        assert type(entry.summoner_id) == str
        assert type(entry.summoner_name) == str
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int
        assert type(entry.mini_series) == utils.classes.MiniSeries

        assert type(entry.mini_series.losses) == int
        assert type(entry.mini_series.progress) == str
        assert type(entry.mini_series.target) == int
        assert type(entry.mini_series.wins) == int
