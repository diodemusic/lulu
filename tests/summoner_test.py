import lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
account_id = os.getenv("ACCOUNT_ID")
name = os.getenv("SUMMONER_NAME")
puuid = os.getenv("PUUID")
summoner_id = os.getenv("SUMMONER_ID")
region = lulu.region.euw


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_by_account():
    by_account_id = lulu.summoner.by_account(region, account_id)

    assert by_account_id.account_id == account_id
    assert by_account_id.summoner_id == summoner_id
    assert by_account_id.name == name
    assert type(by_account_id.profile_icon_id) == int
    assert by_account_id.puuid == puuid
    assert type(by_account_id.revision_date) == int
    assert type(by_account_id.summoner_level) == int


def test_by_name():
    by_name = lulu.summoner.by_name(region, name)

    assert by_name.account_id == account_id
    assert by_name.summoner_id == summoner_id
    assert by_name.name == name
    assert type(by_name.profile_icon_id) == int
    assert by_name.puuid == puuid
    assert type(by_name.revision_date) == int
    assert type(by_name.summoner_level) == int


def test_by_puuid():
    by_puuid = lulu.summoner.by_puuid(region, puuid)

    assert by_puuid.account_id == account_id
    assert by_puuid.summoner_id == summoner_id
    assert by_puuid.name == name
    assert type(by_puuid.profile_icon_id) == int
    assert by_puuid.puuid == puuid
    assert type(by_puuid.revision_date) == int
    assert type(by_puuid.summoner_level) == int


def test_by_summoner_id():
    by_summoner_id = lulu.summoner.by_summoner_id(region, summoner_id)

    assert by_summoner_id.account_id == account_id
    assert by_summoner_id.summoner_id == summoner_id
    assert by_summoner_id.name == name
    assert type(by_summoner_id.profile_icon_id) == int
    assert by_summoner_id.puuid == puuid
    assert type(by_summoner_id.revision_date) == int
    assert type(by_summoner_id.summoner_level) == int
