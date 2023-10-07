import utils


def by_account(region: str, account_id: str) -> object:
    """Get a summoner by account ID.

    Args:
        region (str): Region str.
        account_id (str): Account ID.

    Returns:
        object: Summoner object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{account_id}"
    )

    return utils.classes.Summoner(
        account_id=r["accountId"],
        summoner_id=r["id"],
        name=r["name"],
        profile_icon_id=r["profileIconId"],
        puuid=r["puuid"],
        revision_date=r["revisionDate"],
        summoner_level=r["summonerLevel"],
    )


def by_name(region: str, summoner_name: str) -> object:
    """Get a summoner by summoner name.

    Args:
        region (str): Region str.
        summoner_name (str): Summoner name.

    Returns:
        object: Summoner object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    )

    return utils.classes.Summoner(
        account_id=r["accountId"],
        summoner_id=r["id"],
        name=r["name"],
        profile_icon_id=r["profileIconId"],
        puuid=r["puuid"],
        revision_date=r["revisionDate"],
        summoner_level=r["summonerLevel"],
    )


def by_puuid(region: str, puuid: str) -> object:
    """Get a summoner by PUUID.

    Args:
        region (str): Region str.
        puuid (str): Puuid.

    Returns:
        object: Summoner object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    )

    return utils.classes.Summoner(
        account_id=r["accountId"],
        summoner_id=r["id"],
        name=r["name"],
        profile_icon_id=r["profileIconId"],
        puuid=r["puuid"],
        revision_date=r["revisionDate"],
        summoner_level=r["summonerLevel"],
    )


def by_summoner_id(region: str, summoner_id: str) -> object:
    """Get a summoner by summoner ID.

    Args:
        region (str): Region str
        summoner_id (str): Summoner ID.

    Returns:
        object: Summoner object.
    """

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}"
    )

    return utils.classes.Summoner(
        account_id=r["accountId"],
        summoner_id=r["id"],
        name=r["name"],
        profile_icon_id=r["profileIconId"],
        puuid=r["puuid"],
        revision_date=r["revisionDate"],
        summoner_level=r["summonerLevel"],
    )
