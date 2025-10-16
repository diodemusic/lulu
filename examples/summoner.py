import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")
summoner = api.summoner.by_puuid(Region.EUW, account.puuid)

print(
    f"{account.game_name}#{account.tag_line} is level {summoner.summoner_level}, what a nerd"
)
