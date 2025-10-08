# lulu

lulu is a simple by design Riot API wrapper specifically for League of Legends.

## Installation

WIP

## Features

* Provides a simple, pythonic interface to interact with the Riot API.

## Examples and Documentation

[documentation (not yet implemented)](/)
[examples](https://github.com/diodemusic/lulu/tree/master/examples)

## Example usage

```py
import lulu

api = lulu.Lulu("API_KEY")

account = api.account.by_riot_id(lulu.Continent.EUROPE, "game_name", "tag_line")

print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")
```
