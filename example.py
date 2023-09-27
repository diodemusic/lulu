import lulu.src.lulu as lulu

key = "YOUR_API_KEY"

continent = lulu.continent.europe
region = lulu.region.euw

player = lulu.account_by_riot_id(key, continent, "saves", "000")

sum_score = lulu.mastery_levels_sum_by_puuid(key, region, player.puuid)

print(f"Hi, I'm {player.game_name} and I have {sum_score} total mastery levels :)")
