import utils


def champion_rotations(region: str) -> object:
    """Returns champion rotations, including free-to-play and low-level free-to-play rotations.

    Args:
        region (str): Region str.

    Returns:
        object: ChampionInfo object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/platform/v3/champion-rotations"
    )

    return utils.classes.ChampionInfo(
        free_champion_ids=r["freeChampionIds"],
        free_champion_ids_for_new_players=r["freeChampionIdsForNewPlayers"],
        max_new_player_level=r["maxNewPlayerLevel"],
    )
