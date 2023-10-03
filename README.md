# Lulu

`lulu` is a League of Legends API wrapper built on top of the Riot API.

## Features

* Provides a pythonic, modern, easy to use interface.

* Abstracts away all the API complications.

* Optimised rate limiting ensuring you get the most out of your API key (WIP).

* Optional caching that can be easily configured.

## Example usage

```py
import lulu

settings = lulu.settings.SettingsManager()
settings.set_api_key("API_KEY")
settings.set_cache_enabled(False)
settings.set_cache_ttl(5600)


continent = lulu.continent.europe
region = lulu.region.euw

player = lulu.summoner.by_name(region, "YOUR_NAME_HERE")
sum_score = lulu.mastery.levels_sum_by_puuid(region, player.puuid)

print(f"Hi, I'm {player.name} and I have {sum_score} total mastery levels.")

match_ids = lulu.match.history(continent, player.puuid, 420)
match = lulu.match.by_match_id(continent, match_ids[0])

for participant in match.info.participants:
    if participant["puuid"] == player.puuid:
        print(f"In my last game I had {participant['assists']} assists.")

print(lulu.challenges.config(region))
```

See [`examples/`] for more example usage.

## Docs

(WIP)
