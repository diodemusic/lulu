# lulu

lulu is a Riot API wrapper specifically for League of Legends.

## Features

* Provides a simple, pythonic interface to interact with the Riot API.

## Example usage

```py
import lulu

api = lulu.Lulu("API_KEY")

# Returns AccountDTO {puuid: str, gameName: str?, tagLine: str?}
account = api.account.by_riot_id(lulu.Continent.EUROPE, "game_name", "tag_line")

print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")
```

See [`examples/`] for more example usage.

## Docs

(WIP)
