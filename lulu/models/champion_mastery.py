from pydantic import BaseModel, Field


class NextSeasonMilestones(BaseModel):
    pass


class ChampionMastery(BaseModel):
    puuid: str
    champion_points_until_next_level: int = Field(alias="championPointsUntilNextLevel")
    chest_granted: bool = Field(alias="chestGranted")
    champion_id: int = Field(alias="championId")
    last_play_time: int = Field(alias="lastPlayTime")
    champion_level: int = Field(alias="championLevel")
    champion_points: int = Field(alias="championPoints")
    champion_points_since_last_level: int = Field(alias="championPointsSinceLastLevel")
    mark_required_for_next_level: int = Field(alias="markRequiredForNextLevel")
    champion_season_milestone: int = Field(alias="championSeasonMilestone")
    next_season_milestone: "NextSeasonMilestones" = Field(alias="nextSeasonMilestone")
    tokens_earned: int = Field(alias="tokensEarned")
    milestone_grades: list[str] = Field(alias="milestoneGrades")

    model_config = {"populate_by_name": True}
