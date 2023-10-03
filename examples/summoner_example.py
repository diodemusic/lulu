import lulu


settings = lulu.settings.SettingsManager()
settings.set_api_key("YOUR_API_KEY")
settings.set_cache_enabled(False)


region = lulu.region.euw
summoner = lulu.summoner.by_name(region, "SUMMONER_NAME")


print(f"Object >> {summoner}")
print(f"Level >> {summoner.level}")
print(f"Name >> {summoner.name}")
print(f"Puuid >> {summoner.puuid}")
