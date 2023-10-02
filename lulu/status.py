from . import __utils


def by_region(key: str, region: str) -> object:
    """Get League of Legends status for the given platform.

    Args:
        key (str): Riot API key.
        region (str): Region str.

    Returns:
        object: PlatformStatus object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/status/v4/platform-data",
        key=key,
    )

    return __utils.PlatformStatus(
        platform_id=r["id"],
        incidents=r["incidents"],
        locales=r["locales"],
        maintenances=r["maintenances"],
        name=r["name"],
    )
