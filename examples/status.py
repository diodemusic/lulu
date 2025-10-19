import os

from dotenv import load_dotenv

from pyke import Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

status = api.lol_status.platform_data(Region.EUW)

for incident in status.incidents:
    if incident.incident_severity:
        print(
            f"{incident.incident_severity.name} incident: {incident.titles[0].content}"
        )

        print("Platforms affected:")

        for platform in incident.platforms:
            print(platform.name)

        print("-" * 20)
