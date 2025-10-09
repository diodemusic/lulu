import os

from dotenv import load_dotenv

from pyke import Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

rotations = api.champion.rotations(Region.EUW)

print(f"Max new player level: {rotations.max_new_player_level}")
print(
    f"Free champion ids for new players: {rotations.free_champion_ids_for_new_players}"
)
print(f"Free champion ids: {rotations.free_champion_ids}")
