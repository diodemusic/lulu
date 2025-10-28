import os

from dotenv import load_dotenv

from pyke import Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

# Let's get the current champions in the free rotation
rotations = api.champion.rotations(Region.EUW)

print(f"Max new player level: {rotations.max_new_player_level}")

# The free champions for new players are different
print(
    f"Free champion ids for new players: {rotations.free_champion_ids_for_new_players}"
)

print(f"Free champion ids: {rotations.free_champion_ids}")
