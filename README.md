# Lulu

`lulu` is a League of Legends API wrapper built on top of the Riot API.

## Features

* Provides a pythonic, modern, easy to use interface.

* Abstracts away all the API complications.

## Example usage

```py
import lulu

lu = lulu.Lulu("API_KEY")

# Returns AccountDTO {puuid: str, gameName: str?, tagLine: str?}
account = lulu.account.by_riot_id(lulu.continent.europe, "game_name", "tag_line")
print(f"Player {account.game_name} has the puuid: {account.puuid}")
```

See [`examples/`] for more example usage.

## Docs

(WIP)
