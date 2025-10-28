import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

# Let's get my puuid
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Now my champion masteries
masteries = api.champion_mastery.masteries_by_puuid(Region.EUW, account.puuid)


# Let's print my top ten champion masteries
for mastery in masteries[:10]:
    print(f"Champion ID: {mastery.champion_id}")
    print(f"Champion Level: {mastery.champion_level}")
    print(f"Champion Points: {mastery.champion_points}")

    print("-" * 50)

# And we can get my total champion mastery score
score = api.champion_mastery.score_by_puuid(Region.EUW, account.puuid)
print(f"Player's total champion mastery score: {score}")
