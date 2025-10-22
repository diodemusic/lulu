import os

from dotenv import load_dotenv

from pyke import Continent, Division, Pyke, Queue, Region, Tier

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

# Let's get some plat 2 players
league = api.league.by_queue_tier_division(
    Region.EUW, Queue.SOLO_DUO, Tier.PLATINUM, Division.II
)

champions: dict[str, int] = {}

for player in league[0:49]:
    # Now we get the players last two matches
    match_ids = api.match.match_ids_by_puuid(Continent.EUROPE, player.puuid, count=2)

    # Fetch and analyze each match
    for match_id in match_ids:
        match = api.match.by_match_id(Continent.EUROPE, match_id)

        # Count wins for top and mid champions
        for participant in match.info.participants:
            if participant.team_position == "TOP" or participant.team_position == "MID":
                if participant.champion_name not in champions:
                    champions[participant.champion_name] = 1
                else:
                    champions[participant.champion_name] += 1

# Print the final champion win count dictionary
print(champions)
