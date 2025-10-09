from typing import Optional

from pydantic import BaseModel, Field


class MiniSeries(BaseModel):
    """Maps directly to the Riot API MiniSeriesDTO."""

    losses: int
    progress: str
    target: int
    wins: int

    model_config = {"populate_by_name": True}


class LeagueEntry(BaseModel):
    """Maps directly to the Riot API LeagueEntryDTO."""

    league_id: str = Field(alias="leagueId")
    summoner_id: Optional[str] = Field(alias="summonerId", default=None)
    puuid: str
    queue_type: str = Field(alias="queueType")
    tier: str
    rank: str
    league_points: int = Field(alias="leaguePoints")
    wins: int
    losses: int
    hot_streak: bool = Field(alias="hotStreak")
    veteran: bool
    fresh_blood: bool = Field(alias="freshBlood")
    inactive: bool
    mini_series: Optional[MiniSeries] = Field(alias="miniSeries", default=None)

    model_config = {"populate_by_name": True}
