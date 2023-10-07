import lulu
from dotenv import load_dotenv
import os
import utils


load_dotenv()
key = os.getenv("KEY")
puuid = os.getenv("PUUID")
summoner_id = os.getenv("SUMMONER_ID")


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_by_puuid():
    instances = lulu.clash.by_puuid(puuid)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.Player
        assert type(instance.summoner_id) == str
        assert type(instance.team_id) == str
        assert type(instance.position) == str
        assert type(instance.role) == str


def test_by_summoner():
    instances = lulu.clash.by_summoner(summoner_id)

    assert type(instances) == list

    for instance in instances:
        assert type(instance) == utils.classes.Player
        assert type(instance.summoner_id) == str
        assert type(instance.team_id) == str
        assert type(instance.position) == str
        assert type(instance.role) == str


# def test_teams():
#     instance = lulu.clash.teams()  # (team_id)

#     assert type(instance) == utils.classes.ClashTeam
#     assert type(instance.team_id) == int
#     assert type(instance.name) == str
#     assert type(instance.icon_id) == int
#     assert type(instance.tier) == int
#     assert type(instance.captain) == str
#     assert type(instance.abbreviation) == str
#     assert type(instance.players) == list

#     for player in instance.players:
#         assert type(player) == utils.classes.Player
#         assert type(player.summoner_id) == str
#         assert type(player.position) == str
#         assert type(player.role) == str
