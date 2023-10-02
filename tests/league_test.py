import lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
summoner_id = os.getenv("SUMMONER_ID")
region = lulu.region.euw
queue = lulu.queue.solo_duo
tier = lulu.tier.gold
division = lulu.division.two


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_challenger():
    challengers = lulu.league.challenger(region, queue)

    assert type(challengers.name) == str
    assert type(challengers.entries) == list
    assert type(challengers.league_id) == str
    assert challengers.queue == queue
    assert challengers.tier == "CHALLENGER"

    for entry in challengers.entries:
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_points) == int
        assert type(entry.losses) == int
        assert entry.rank == "I"
        assert type(entry.summoner_id) == str
        assert type(entry.summoner_name) == str
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int


def test_by_summoner_id():
    entries = lulu.league.by_summoner_id(region, summoner_id)

    assert type(entries) == list

    for entry in entries:
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_id) == str
        assert type(entry.points) == int
        assert type(entry.losses) == int
        assert type(entry.queue_type) == str
        assert type(entry.rank) == str
        assert entry.summoner_id == summoner_id
        assert type(entry.summoner_name) == str
        assert type(entry.tier) == str
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int


def test_by_queue_tier_division():
    entries = lulu.league.by_queue_tier_division(
        region,
        queue,
        tier,
        division,
    )

    assert type(entries) == list

    for entry in entries:
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_id) == str
        assert type(entry.points) == int
        assert type(entry.losses) == int
        assert entry.queue_type == queue
        assert entry.rank == division
        assert type(entry.summoner_id) == str
        assert type(entry.summoner_name) == str
        assert entry.tier == tier
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int


def test_grandmaster():
    grandmasters = lulu.league.grandmaster(region, queue)

    assert type(grandmasters.name) == str
    assert type(grandmasters.entries) == list
    assert type(grandmasters.league_id) == str
    assert grandmasters.queue == queue
    assert grandmasters.tier == "GRANDMASTER"

    for entry in grandmasters.entries:
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_points) == int
        assert type(entry.losses) == int
        assert entry.rank == "I"
        assert type(entry.summoner_id) == str
        assert type(entry.summoner_name) == str
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int


def test_by_league_id():
    league_id = "d472b83c-2a7c-4fdd-91ae-76713eb00cdd"
    league_list = lulu.league.by_league_id(region, league_id)

    assert type(league_list.name) == str
    assert type(league_list.entries) == list
    assert league_list.league_id == league_id
    assert type(league_list.queue) == str
    assert type(league_list.tier) == str

    for entry in league_list.entries:
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


def test_master():
    masters = lulu.league.master(region, queue)

    assert type(masters.name) == str
    assert type(masters.entries) == list
    assert type(masters.league_id) == str
    assert masters.queue == queue
    assert masters.tier == "MASTER"

    for entry in masters.entries:
        assert type(entry.fresh_blood) == bool
        assert type(entry.hot_streak) == bool
        assert type(entry.inactive) == bool
        assert type(entry.league_points) == int
        assert type(entry.losses) == int
        assert entry.rank == "I"
        assert type(entry.summoner_id) == str
        assert type(entry.summoner_name) == str
        assert type(entry.veteran) == bool
        assert type(entry.wins) == int