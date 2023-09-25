# Lulu
An API wrapper for the Riot API.

Lulu provides a pythonic easy to use interface.

## Lulu handles

* Optimised rate limiting ensuring you get the most out of your API key.

* Caching so you never have to make the same call twice.

* Enums for all common params eg. regions, continents and ranks.

## Example usage

```py
import lulu.src.lulu as lulu

key = "YOUR_RIOT_API_KEY"

continent = lulu.continent.europe
region = lulu.region.euw

player = lulu.account_by_riot_id(key, continent, "saves", "000")

mastery_entries = lulu.mastery_by_puuid(key, region, player.puuid)
mastery_points_sum = sum(entry.points for entry in mastery_entries)

print(f"hi im {player.game_name} and i have {mastery_points_sum} total mastery :)")
```
