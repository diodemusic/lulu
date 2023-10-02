from . import __utils


def by_account(key: str, region: str, account_id: str) -> object:
    """Get a summoner by account ID.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        account_id (str): Account ID.

    Returns:
        object: Summoner object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{account_id}",
        key=key,
    )

    return __utils.Summoner(
        account_id=r["accountId"],
        summoner_id=r["id"],
        name=r["name"],
        profile_icon_id=r["profileIconId"],
        puuid=r["puuid"],
        revision_date=r["revisionDate"],
        level=r["summonerLevel"],
    )


def by_name(key: str, region: str, summoner_name: str) -> object:
    """Get a summoner by summoner name.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        summoner_name (str): Summoner name.

    Returns:
        object: Summoner object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}",
        key=key,
    )

    return __utils.Summoner(
        account_id=r["accountId"],
        summoner_id=r["id"],
        name=r["name"],
        profile_icon_id=r["profileIconId"],
        puuid=r["puuid"],
        revision_date=r["revisionDate"],
        level=r["summonerLevel"],
    )


def by_puuid(key: str, region: str, puuid: str) -> object:
    """Get a summoner by PUUID.

    Args:
        key (str): Riot API key.
        region (str): Region str.
        puuid (str): Puuid.

    Returns:
        object: Summoner object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}",
        key=key,
    )

    return __utils.Summoner(
        account_id=r["accountId"],
        summoner_id=r["id"],
        name=r["name"],
        profile_icon_id=r["profileIconId"],
        puuid=r["puuid"],
        revision_date=r["revisionDate"],
        level=r["summonerLevel"],
    )


def by_summoner_id(key: str, region: str, summoner_id: str) -> object:
    """Get a summoner by summoner ID.

    Args:
        key (str): Riot API key.
        region (str): Region str
        summoner_id (str): Summoner ID.

    Returns:
        object: Summoner object.
    """

    r = __utils.call(
        url=f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}",
        key=key,
    )

    return __utils.Summoner(
        account_id=r["accountId"],
        summoner_id=r["id"],
        name=r["name"],
        profile_icon_id=r["profileIconId"],
        puuid=r["puuid"],
        revision_date=r["revisionDate"],
        level=r["summonerLevel"],
    )
