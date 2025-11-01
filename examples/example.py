import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, exceptions

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

# Initialize the API
api = Pyke(API_KEY)

# Every pyke method follows the same convention as the Riot API
# For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes:
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Every response is a Pydantic model with dot notation access
print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID:   {account.puuid}")

# Pydantic models provide convenient serialization
print(account.model_dump_json())  # JSON string
print(account.model_dump())  # Python dictionary

# pyke throws typed exceptions matching Riot API error codes
try:
    region = api.account.region_by_puuid(Continent.EUROPE, account.puuid)
except exceptions.DataNotFound as e:
    print(e)  # Output: Data not found (Error Code: 404)
    quit()

print(f"PUUID:  {region.puuid}")
print(f"Game:   {region.game}")
print(f"Region: {region.region}")
