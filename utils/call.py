from utils import caching
import logging
import requests
import time
from lulu.settings import SettingsManager


settings_manager = SettingsManager()


def make_call(url: str, max_retries: int = 3, retry_delay: int = 40):
    cache_key = (
        url.split("https://")[1].replace(".", "_").replace("/", "_").replace("?", "_")
    )

    cached_response = caching.load_from_cache(cache_key=cache_key)

    if cached_response is not None:
        print(cache_key)

        return cached_response

    headers = {"X-Riot-Token": settings_manager.get_api_key()}

    for retry in range(max_retries + 1):
        print(url)

        r = requests.get(url, headers=headers)
        time.sleep(0.6)

        if r.status_code == 200:
            r_dict = r.json()

            caching.save_to_cache(cache_data=r_dict, cache_key=cache_key)

            return r_dict

        elif r.status_code == 429:
            logging.warning(
                f"Rate limited, Waiting {int(r.headers.get('Retry-After'))} seconds..."
            )

            time.sleep(int(r.headers.get("Retry-After")))

        elif r.status_code == 404:
            raise Exception("Error 404.")

        elif r.status_code == 403:
            raise Exception("Error 403, check API key.")

        else:
            logging.error(f"Status code >> {r.status_code}.")

            if retry < max_retries:
                logging.info(f"Retrying in {retry_delay} seconds...")

                time.sleep(retry_delay)

            else:
                raise Exception("Max retries reached, giving up.")
