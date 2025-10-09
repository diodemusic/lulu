import os

from dotenv import load_dotenv

from pyke import Division, Pyke, Queue, Region, Tier

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

league_entries = api.league_exp.entries_by_queue_tier_division(
    Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
)

for league_entry in league_entries:
    print(f"Rank: {league_entry.rank}")
    print(f"League points: {league_entry.league_points}")
    print(f"Wins: {league_entry.wins}")

    print("-" * 50)
