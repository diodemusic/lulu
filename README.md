# lulu

**lulu** is a simple-by-design Riot API wrapper specifically for League of Legends.

## Installation

WIP

## Features

- Provides a simple, pythonic interface to interact with the Riot API.

## Documentation & Examples

- [Documentation (WIP)](/)
- [Examples](https://github.com/diodemusic/lulu/tree/master/examples)

## Example Usage

```py
import lulu

# We always initialize the API like this
# Check the examples for loading an api key from a .env file
api = lulu.Lulu("API_KEY")

# Every lulu method follows the same convention as the Riot API
# For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes the following
account = api.account.by_riot_id(lulu.Continent.EUROPE, "game_name", "tag_line")

# Every response is a pydantic model whose members can be accessed with dot notation
print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")

# lulu throws custom exceptions, again following the same conventions as the Riot API
# For example a request that responds with error code 429
# Will throw lulu.exceptions.RateLimitExceeded
try:
    region = api.account.region_by_puuid(lulu.Continent.EUROPE, account.puuid)
except lulu.exceptions.RateLimitExceeded as e:
    print(e)  # Output: Rate limit exceeded (Error Code: 429)
    quit()

# Members can be accessed with dot notation just like before
print(f"PUUID: {region.puuid}")
print(f"Game: {region.game}")
print(f"Region: {region.region.value}")
```

enjoy :)
