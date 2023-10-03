# Lulu
`lulu` is a League of Legends API wrapper for the Riot API.

`lulu` provides a pythonic, modern, easy to use interface.

## Lulu handles

* Optimised rate limiting ensuring you get the most out of your API key.

* Caching so you never have to make the same call twice.

## Example usage

```py
import lulu

settings = lulu.settings.SettingsManager()
settings.set_api_key("API_KEY")
settings.set_cache_enabled(False)


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

Pending...
