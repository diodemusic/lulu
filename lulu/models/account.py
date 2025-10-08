from pydantic import BaseModel, Field

from ..enums.region import Region


class Account(BaseModel):
    puuid: str
    game_name: str = Field(alias="gameName")
    tag_line: str = Field(alias="tagLine")

    model_config = {"populate_by_name": True}


class AccountRegion(BaseModel):
    puuid: str
    game: str = "lol"
    region: Region
