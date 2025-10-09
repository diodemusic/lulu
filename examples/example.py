import os

from dotenv import load_dotenv

from lulu import Continent, Lulu, exceptions

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

# We always initialize the API like this
api = Lulu(API_KEY)

# Every lulu method follows the same convention as the Riot API
# For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes the following
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Every response is a pydantic model whose members can be accessed with dot notation
print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")

# lulu throws custom exceptions, again following the same conventions as the Riot API
# For example a request that responds with error code 429
# Will throw exceptions.RateLimitExceeded
try:
    region = api.account.region_by_puuid(Continent.EUROPE, account.puuid)
except exceptions.RateLimitExceeded as e:
    print(e)  # Output: Rate limit exceeded (Error Code: 429)
    quit()

# Members can be accessed with dot notation just like before
print(f"PUUID: {region.puuid}")
print(f"Game: {region.game}")
print(f"Region: {region.region.value}")
