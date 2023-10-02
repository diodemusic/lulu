import os
import pickle
import time
from lulu.settings import SettingsManager


settings_manager = SettingsManager()


if settings_manager.cache_enabled == True:
    cache_dir = "cache"

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)


def save_to_cache(cache_data, cache_key: str):
    if settings_manager.cache_enabled == True:
        cache_path = os.path.join(cache_dir, f"{cache_key}.pkl")
        cache_data = {"data": cache_data, "timestamp": int(time.time())}

        with open(cache_path, "wb") as cfp:
            pickle.dump(cache_data, cfp)


def load_from_cache(cache_key: str):
    if settings_manager.cache_enabled == True:
        cache_path = os.path.join(cache_dir, f"{cache_key}.pkl")

        if os.path.exists(cache_path):
            with open(cache_path, "rb") as cfp:
                cache_data = pickle.load(cfp)

                if (
                    int(time.time()) - cache_data["timestamp"]
                    <= settings_manager.cache_ttl
                ):
                    return cache_data["data"]

        return None
