import lulu


settings = lulu.settings.SettingsManager()
settings.set_api_key("YOUR_API_KEY")
settings.set_cache_enabled(False)


region = lulu.region.euw
status = lulu.status.by_region(region)


print(f"Object >> {status}")
print(f"Incidents >> {status.incidents}")
print(f"Platform ID >> {status.platform_id}")
