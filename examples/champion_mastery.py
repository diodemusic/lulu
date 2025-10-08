import os

from dotenv import load_dotenv

import lulu

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = lulu.Lulu(API_KEY)
REGION = lulu.Region.EUW

account = api.account.by_riot_id(lulu.Continent.EUROPE, "saves", "000")

champion_masteries = api.champion_mastery.masteries_by_puuid(REGION, account.puuid)

for champion_mastery in champion_masteries:
    print(f"Champion ID: {champion_mastery.champion_id}")
    print(f"Champion Level: {champion_mastery.champion_level}")
    print(f"Champion Points: {champion_mastery.champion_points}")

    print("-" * 50)

CHAMPION_ID = 11

try:
    champion_mastery = api.champion_mastery.by_puuid_and_champion_id(
        REGION, account.puuid, CHAMPION_ID
    )
except lulu.exceptions.DataNotFound as e:
    print(f"Champion id {CHAMPION_ID} not found: {e}")
    quit()

print(f"Champion ID: {champion_mastery.champion_id}")
print(f"Champion Level: {champion_mastery.champion_level}")
print(f"Champion Points: {champion_mastery.champion_points}")
