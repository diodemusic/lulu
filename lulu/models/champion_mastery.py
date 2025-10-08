from typing import Optional

from pydantic import BaseModel, Field


class RewardConfig(BaseModel):
    """Maps directly to the Riot API RewardConfigDTO."""

    reward_value: str = Field(alias="rewardValue")
    reward_type: str = Field(alias="rewardType")
    maximum_reward: int = Field(alias="maximumReward")


class NextSeasonMilestones(BaseModel):
    """Maps directly to the Riot API NextSeasonMilestonesDTO."""

    require_grade_counts: object = Field(alias="requireGradeCounts")
    reward_marks: int = Field(alias="rewardMarks")
    bonus: bool
    reward_config: Optional[RewardConfig] = Field(alias="rewardConfig", default=None)


class ChampionMastery(BaseModel):
    """Maps directly to the Riot API ChampionMasteryDTO."""

    puuid: str
    champion_points_until_next_level: int = Field(alias="championPointsUntilNextLevel")
    chest_granted: Optional[bool] = Field(alias="chestGranted", default=None)
    champion_id: int = Field(alias="championId")
    last_play_time: int = Field(alias="lastPlayTime")
    champion_level: int = Field(alias="championLevel")
    champion_points: int = Field(alias="championPoints")
    champion_points_since_last_level: int = Field(alias="championPointsSinceLastLevel")
    mark_required_for_next_level: int = Field(alias="markRequiredForNextLevel")
    champion_season_milestone: int = Field(alias="championSeasonMilestone")
    next_season_milestones: Optional[NextSeasonMilestones] = Field(
        alias="nextSeasonMilestone", default=None
    )
    tokens_earned: int = Field(alias="tokensEarned")
    milestone_grades: Optional[list[str]] = Field(alias="milestoneGrades", default=None)

    model_config = {"populate_by_name": True}
