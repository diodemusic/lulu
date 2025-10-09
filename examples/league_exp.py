import os

from dotenv import load_dotenv

from lulu import Division, Lulu, Queue, Region, Tier

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Lulu(API_KEY)

league_entries = api.league_exp.entries_by_queue_tier_division(
    Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
)

for league_entry in league_entries:
    print(f"League id: {league_entry.league_id}")
    print(f"Summoner id: {league_entry.summoner_id}")
    print(f"PUUID: {league_entry.puuid}")
    print(f"Queue type: {league_entry.queue_type}")
    print(f"Tier: {league_entry.tier}")
    print(f"Rank: {league_entry.rank}")
    print(f"League points: {league_entry.league_points}")
    print(f"Wins: {league_entry.wins}")
    print(f"Losses: {league_entry.losses}")
    print(f"Hot streak: {league_entry.hot_streak}")
    print(f"Veteran: {league_entry.veteran}")
    print(f"Fresh blood: {league_entry.fresh_blood}")
    print(f"Inactive: {league_entry.inactive}")
    print(f"Mini series: {league_entry.mini_series}")

    print("-" * 50)
