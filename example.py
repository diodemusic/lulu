import lulu

lu = lulu.SetKey("YOUR_KEY_HERE")

player = lu.account.by_riot_id(lulu.Continent.europe, "saves", "000")
mastery_entries = lu.champion_mastery.by_puuid(lulu.Region.euw, player.puuid)
mastery_points_sum = sum(entry.points for entry in mastery_entries)

print(f"Hi, I'm {player.game_name} and I have {mastery_points_sum} total mastery :)")
