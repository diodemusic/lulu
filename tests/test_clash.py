from pyke import Pyke, Region
from pyke.models.clash_v1 import PlayerDto, TeamDto, TournamentDto

from .base import TEST_PUUID, TEST_TEAM_ID, TEST_TOURNAMENT_ID, api

if not TEST_PUUID:
    quit()

if not TEST_TEAM_ID:
    quit()

if not TEST_TOURNAMENT_ID:
    quit()


def test_by_puuid(api: Pyke):
    by_puuid = api.clash.by_puuid(Region.EUW, TEST_PUUID)

    for player in by_puuid:
        assert isinstance(player, PlayerDto)


def test_by_team_id(api: Pyke):
    by_team_id = api.clash.by_team_id(Region.EUW, TEST_TEAM_ID)

    assert isinstance(by_team_id, TeamDto)


def test_tournaments(api: Pyke):
    tournaments = api.clash.tournaments(Region.EUW)

    for tournament in tournaments:
        assert isinstance(tournament, TournamentDto)


def test_tournament_by_team_id(api: Pyke):
    tournament_by_team_id = api.clash.tournament_by_team_id(Region.EUW, TEST_TEAM_ID)

    assert isinstance(tournament_by_team_id, TournamentDto)


def test_tournament_by_tournament_id(api: Pyke):
    tournament_by_tournament_id = api.clash.tournament_by_tournament_id(
        Region.EUW, TEST_TOURNAMENT_ID
    )

    assert isinstance(tournament_by_tournament_id, TournamentDto)
