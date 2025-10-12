import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, Queue, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)


challenger_leagues = api.league.challenger_leagues_by_queue(
    region=Region.EUW, queue=Queue.SOLO_DUO
)

for challenger_player in challenger_leagues.entries[0:5]:
    account = api.account.by_puuid(
        continent=Continent.EUROPE, puuid=challenger_player.puuid
    )
    riot_id = f"{account.game_name}#{account.tag_line}"

    print(
        f"{riot_id} has {challenger_player.wins} wins and {challenger_player.losses} losses."
    )
