import utils


def platform_data(region: str) -> object:
    """Get League of Legends status for the given platform.

    Args:
        region (str): Region str.

    Returns:
        object: PlatformData object.
    """

    incident_entries = []
    maintenance_entries = []

    r = utils.call.make_call(
        url=f"https://{region}.api.riotgames.com/lol/status/v4/platform-data"
    )

    for incident in r["incidents"]:
        incident_entries.append(
            utils.classes.Status(
                status_id=incident["statusId"],
                maintenance_status=incident["maintenanceStatus"],
                incident_severity=incident["incidentSeverity"],
                titles=incident["titles"],
                updates=incident["updates"],
                created_at=incident["createdAt"],
                archive_at=incident["archiveAt"],
                updated_at=incident["updatedAt"],
                platforms=incident["platforms"],
            ),
        )

    for maintenance in r["maintenances"]:
        maintenance_entries.append(
            utils.classes.Status(
                status_id=maintenance["statusId"],
                maintenance_status=maintenance["maintenanceStatus"],
                incident_severity=maintenance["incidentSeverity"],
                titles=maintenance["titles"],
                updates=maintenance["updates"],
                created_at=maintenance["createdAt"],
                archive_at=maintenance["archiveAt"],
                updated_at=maintenance["updatedAt"],
                platforms=maintenance["platforms"],
            ),
        )

    return utils.classes.PlatformData(
        platform_id=r["id"],
        incidents=incident_entries,
        locales=r["locales"],
        maintenances=maintenance_entries,
        name=r["name"],
    )
