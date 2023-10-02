# Lulu
An API wrapper for the Riot API.

Lulu provides a pythonic easy to use interface.

## Lulu handles

* Optimised rate limiting ensuring you get the most out of your API key.

* Caching so you never have to make the same call twice.

## Example usage

```py
import lulu

key = "YOUR_RIOT_API_KEY"

continent = lulu.continent.europe
region = lulu.region.euw

player = lulu.account.by_riot_id(key, continent, "john_doe", "1234")
sum_score = lulu.mastery.levels_sum_by_puuid(key, region, player.puuid)

print(f"Hi, I'm {player.game_name} and I have {sum_score} total mastery levels.")

match_ids = lulu.match.history(key, continent, player.puuid, 420)
match = lulu.match.by_match_id(key, continent, match_ids[0])

for participant in match.info.participants:
    if participant["puuid"] == player.puuid:
        print(f"In my last game I had {participant['assists']} assists.")
```
