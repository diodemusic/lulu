import utils


def by_region(region: str) -> object:
    """Get League of Legends status for the given platform.

    Args:
        region (str): Region str.

    Returns:
        object: PlatformStatus object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/status/v4/platform-data"
    )

    return utils.classes.PlatformStatus(
        platform_id=r["id"],
        incidents=r["incidents"],
        locales=r["locales"],
        maintenances=r["maintenances"],
        name=r["name"],
    )
