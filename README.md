# Lulu
An API wrapper for the Riot API.

Lulu provides a pythonic easy to use interface.

## Lulu handles

* Optimised rate limiting ensuring you get the most out of your API key.

* Caching so you never have to make the same call twice.

## Example usage

```py
from lulu import continent, region, account, mastery, match

key = "YOUR_RIOT_API_KEY"

continent = continent.europe
region = region.euw

player = account.by_riot_id(key, continent, "john_doe", "1234")
sum_score = mastery.levels_sum_by_puuid(key, region, player.puuid)

print(f"Hi, I'm {player.game_name} and I have {sum_score} total mastery levels.")

match_ids = match.history(key, continent, player.puuid, 420)
match = match.by_match_id(key, continent, match_ids[0])

for participant in match.info.participants:
    if participant["puuid"] == player.puuid:
        print(f"In my last game I had {participant['assists']} assists.")
```
