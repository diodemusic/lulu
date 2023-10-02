from . import __utils


def free_rotation(key: str, region: str) -> object:
    """Returns champion rotations, including free-to-play and low-level free-to-play rotations.

    Args:
        key (str): Riot API key.
        region (str): Region str.

    Returns:
        object: FreeChampionRotation object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/platform/v3/champion-rotations",
        key=key,
    )

    return __utils.FreeChampionRotation(
        free_champion_ids=r["freeChampionIds"],
        free_champion_ids_for_new_players=r["freeChampionIdsForNewPlayers"],
        max_new_player_level=r["maxNewPlayerLevel"],
    )
