from enum import Enum


class Type(Enum):
    """# Type of match"""

    RANKED = "ranked"
    NORMAL = "normal"
    TOURNEY = "tourney"
    TUTORIAL = "tutorial"
