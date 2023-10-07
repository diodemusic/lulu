from utils import caching
import logging
import requests
import time
from lulu.settings import SettingsManager


settings_manager = SettingsManager()


class NotFoundError(Exception):
    pass


class ApiKeyError(Exception):
    pass


def make_call(url: str, retry_delay: int = 120):
    start_time = time.time()

    cache_key = (
        url.split("https://")[1].replace(".", "_").replace("/", "_").replace("?", "_")
    )

    cached_response = caching.load_from_cache(cache_key=cache_key)

    if cached_response is not None:
        print(cache_key)
        return cached_response

    print(url)

    headers = {"X-Riot-Token": settings_manager.get_api_key()}

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        app_rate_limit = r.headers.get("X-App-Rate-Limit").split(",")

        time_to_wait = int(app_rate_limit[1].split(":")[1]) / int(
            app_rate_limit[1].split(":")[0]
        )

        elapsed_time = time.time() - start_time

        if elapsed_time < time_to_wait:
            time.sleep(time_to_wait - elapsed_time)

        app_rate_limit_count = (
            r.headers.get("X-App-Rate-Limit-Count").split(",")[1].split(":")
        )

        print(
            f"Rate limit : {app_rate_limit_count[0]} / {app_rate_limit[1].split(':')[0]}"
        )

        r_dict = r.json()
        caching.save_to_cache(cache_data=r_dict, cache_key=cache_key)

        return r_dict

    elif r.status_code == 429:
        retry_after_header = r.headers.get("Retry-After")

        if retry_after_header:
            retry_after_seconds = int(retry_after_header)
            logging.warning(f"Error 429, Waiting {retry_after_seconds} seconds...")
            time.sleep(retry_after_seconds)

        else:
            logging.warning("Rate limited, Waiting for default time...")
            time.sleep(retry_delay)

    elif r.status_code == 404:
        raise NotFoundError("Error 404, data not found.")

    elif r.status_code == 403:
        raise ApiKeyError("Error 403, check API key.")

    else:
        raise Exception(f"Error {r.status_code}.")
