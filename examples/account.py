import os

from dotenv import load_dotenv

from pyke import Continent, Pyke

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)
CONTINENT = Continent.EUROPE

account = api.account.by_riot_id(CONTINENT, "saves", "000")

print(f"PUUID: {account.puuid}")
print(f"Game name: {account.game_name}")
print(f"Tag line: {account.tag_line}")

region = api.account.region_by_puuid(CONTINENT, account.puuid)

print(f"PUUID: {region.puuid}")
print(f"Game: {region.game}")
print(f"Region: {region.region.value}")
