# lulu
An API wrapper for the Riot API.

lulu provides a pythonic easy to use interface.

All endpoints fully unit tested.

## lulu handles

* Optimised rate limiting ensuring you get the most out of your API key.

* Caching so you never have to make the same call twice.

* Enums for all common params eg. regions, continents and ranks.

## Example usage

```py
import lulu

lu = lulu.set_key("YOUR_KEY_HERE")

player = lu.account.by_riot_id(lulu.Continent.europe, "saves", "000")
mastery_entries = lu.champion_mastery.by_puuid(lulu.Region.euw, player.puuid)
mastery_points_sum = sum(entry.points for entry in mastery_entries)

print(f"Hi, I'm {player.game_name} and I have {mastery_points_sum} total mastery :)")
```
