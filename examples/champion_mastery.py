import os

from dotenv import load_dotenv

import lulu

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = lulu.Lulu(API_KEY)
REGION = lulu.Region.EUW

account = api.account.by_riot_id(lulu.Continent.EUROPE, "saves", "000")

champion_masteries = api.champion_mastery.masteries_by_puuid(REGION, account.puuid)

for champion_mastery in champion_masteries:
    print(f"PUUID: {champion_mastery.puuid}")
    print(f"Champion ID: {champion_mastery.champion_id}")
    print(f"Champion Level: {champion_mastery.champion_level}")
    print(f"Champion Points: {champion_mastery.champion_points}")
    print(
        f"Points Since Last Level: {champion_mastery.champion_points_since_last_level}"
    )
    print(
        f"Points Until Next Level: {champion_mastery.champion_points_until_next_level}"
    )
    print(
        f"Mark Required for Next Level: {champion_mastery.mark_required_for_next_level}"
    )
    print(f"Tokens Earned: {champion_mastery.tokens_earned}")
    print(f"Chest Granted: {champion_mastery.chest_granted}")
    print(f"Champion Season Milestone: {champion_mastery.champion_season_milestone}")
    print(f"Milestone Grades: {champion_mastery.milestone_grades}")
    print(f"Last Play Time: {champion_mastery.last_play_time}")

    if champion_mastery.next_season_milestones:
        print("Next Season Milestone:")
        print(
            f"  Require Grade Counts: {champion_mastery.next_season_milestones.require_grade_counts}"
        )
        print(f"  Reward Marks: {champion_mastery.next_season_milestones.reward_marks}")
        print(f"  Bonus: {champion_mastery.next_season_milestones.bonus}")
    else:
        print("Next Season Milestone: None")

    print("-" * 50)
