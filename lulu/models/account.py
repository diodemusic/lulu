from pydantic import BaseModel


class Account(BaseModel):
    puuid: str
    game_name: str
    tag_line: str
