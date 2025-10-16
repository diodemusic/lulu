from pyke import Pyke, Region
from pyke._models.spectator_v5 import CurrentGameInfo, FeaturedGames

from .base import TEST_PUUID, api

if not TEST_PUUID:
    quit()


# def test_by_puuid(api: Pyke):
#     by_puuid = api.spectator.by_puuid(
#         region=Region.EUW,
#         puuid=TEST_PUUID,
#     )

#     assert isinstance(by_puuid, CurrentGameInfo)
