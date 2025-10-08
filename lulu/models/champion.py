from pydantic import BaseModel, Field


class ChampionInfo(BaseModel):
    """Maps directly to the Riot API ChampionInfoDTO."""

    max_new_player_level: int = Field(alias="maxNewPlayerLevel")
    free_champion_ids_for_new_players: list[int] = Field(
        alias="freeChampionIdsForNewPlayers"
    )
    free_champion_ids: list[int] = Field(alias="freeChampionIds")

    model_config = {"populate_by_name": True}
