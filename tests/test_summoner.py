from pyke import Region, Pyke
from pyke._models.summoner_v4 import SummonerDTO

from .base import TEST_PUUID, api

if not TEST_PUUID:
    quit()


def test_by_puuid(api: Pyke):
    by_puuid = api.summoner.by_puuid(
        region=Region.EUW,
        puuid=TEST_PUUID,
    )

    assert isinstance(by_puuid, SummonerDTO)
