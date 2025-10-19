import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

# Let's not print urls, we don't want our clash team to be filled with random urls
api = Pyke(API_KEY, print_url=False)

# Let's check if there is currently a clash
clashes = api.clash.tournaments(Region.EUW)

if clashes:
    clash = clashes[0]
else:
    print("There are currently no clashes planned/running")
    quit()

# If there is a clash, let's see what position we are playing
# We will need our puuid
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# We can get our clash team like this
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")
players = api.clash.by_puuid(Region.EUW, account.puuid)

if not players:
    print("You are not in an active clash team")
    quit()

# Let's print what roles everyone is playing
for player in players:
    if player.puuid == account.puuid:
        # We already know our own riot id from the account call we made, no need to get it again
        riot_id = f"{account.game_name}#{account.tag_line}"
    else:
        # For everyone else let's convert puuid to riot id
        team_mate_account = api.account.by_puuid(Continent.EUROPE, player.puuid)
        riot_id = f"{account.game_name}#{account.tag_line}"

    # Finally we can print our riot id and role
    print(f"{riot_id} is playing the {player.position.value} role.")
