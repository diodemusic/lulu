import lulu
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
name = os.getenv("SUMMONER_NAME")


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


region = lulu.region.euw
summoner = lulu.summoner.by_name(region, name)


print(f"Object >> {summoner}")
print(f"Level >> {summoner.level}")
print(f"Name >> {summoner.name}")
print(f"Puuid >> {summoner.puuid}")
