import os

from dotenv import load_dotenv

import lulu

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = lulu.Lulu(API_KEY)
REGION = lulu.Region.EUW

account = api.account.by_riot_id(lulu.Continent.EUROPE, "saves", "000")

champion_masteries = api.champion_mastery.masteries_by_puuid(REGION, account.puuid)

print(champion_masteries)
