import lulu.src.lulu as lulu

key = "YOUR_RIOT_API_KEY"

continent = lulu.continent.europe
region = lulu.region.euw

player = lulu.account_by_riot_id(key, continent, "saves", "000")

mastery_entries = lulu.mastery_by_puuid(key, region, player.puuid)
mastery_points_sum = sum(entry.points for entry in mastery_entries)

print(f"hi im {player.game_name} and i have {mastery_points_sum} total mastery :)")
