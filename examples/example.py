import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, exceptions

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

# We always initialize the API like this
# We can explicitly disable url logging, by default pyke will print the url of all api calls
api = Pyke(API_KEY, print_url=False)

# Every pyke method follows the same convention as the Riot API
# For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes the following
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Every response is a pydantic model whose members can be accessed with dot notation
print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")

# We get access to all the methods that come with a pydantic model
# For example a json string
print(account.model_dump_json())
# Or a python dictionary
print(account.model_dump())

# pyke throws custom exceptions, again following the same conventions as the Riot API
# For example a request that responds with error code 429
# Will throw pyke.exceptions.RateLimitExceeded
try:
    region = api.account.region_by_puuid(Continent.EUROPE, account.puuid)
except exceptions.DataNotFound as e:
    print(e)  # Output: Data not found (Error Code: 404)
    quit()

# Members can be accessed with dot notation just like before
print(f"PUUID: {region.puuid}")
print(f"Game: {region.game}")
print(f"Region: {region.region}")
