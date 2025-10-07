# lulu

lulu is a Riot API wrapper specifically for League of Legends.

## Features

* Provides a simple, pythonic interface to interact with the Riot API.

## Example usage

```py
from lulu import Lulu, Continent

lu = Lulu("API_KEY")

CONTINENT = Continent.europe.value

# Returns AccountDTO {puuid: str, gameName: str?, tagLine: str?}
account = lu.account_by_riot_id(CONTINENT, "game_name", "tag_line")

print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")
```

See [`examples/`] for more example usage.

## Docs

(WIP)
