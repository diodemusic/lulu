"""[![PyPI - Version](https://img.shields.io/pypi/v/pyke-lol)](https://pypi.org/project/pyke-lol/)
[![Documentation](https://img.shields.io/badge/Documentation-blue)](https://diodemusic.github.io/pyke/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyke-lol)](https://pypi.org/project/pyke-lol/)
![Coverage](https://img.shields.io/badge/Coverage-94%25-brightgreen.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/diodemusic/pyke/blob/main/LICENCE.txt)

**pyke** is an opinionated, simple-by-design Riot API wrapper with smart rate limiting specifically for League of Legends.

---

## Installation

Install the latest version directly from PyPI:

```bash
pip install pyke-lol
```

---

## Quickstart

```py
from pyke import Continent, Pyke, exceptions

# We always initialize the API like this
api = Pyke("API_KEY")

# Every pyke method follows the same convention as the Riot API
# For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes the following
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Every response is a pydantic model whose members can be accessed with dot notation
print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")

# We get access to all the methods that come with a pydantic model
# For example a json string
print(account.model_dump_json())
# Or a python dictionary
print(account.model_dump())

# pyke throws custom exceptions, again following the same conventions as the Riot API
# For example a request that responds with error code 429
# Will throw pyke.exceptions.RateLimitExceeded
try:
    region = api.account.region_by_puuid(Continent.EUROPE, account.puuid)
except exceptions.DataNotFound as e:
    print(e)  # Output: Data not found (Error Code: 404)
    quit()

# Members can be accessed with dot notation just like before
print(f"PUUID: {region.puuid}")
print(f"Game: {region.game}")
print(f"Region: {region.region}")
```

> **Note:** You need Python 3.9+ to use pyke.

---

## Logging

```py
import logging
import os

from dotenv import load_dotenv

from pyke import Continent, Pyke

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

# Configure logging BEFORE creating the Pyke instance
# This is the standard Python way to enable logging for all libraries
logging.basicConfig(
    level=logging.INFO,  # Show INFO, WARNING, and ERROR logs
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

# Logging levels from least to most severe:
# - DEBUG: Detailed diagnostic information (not used in this example)
# - INFO: Request URLs, rate limit tracking (e.g., "(45/100) - https://...")
# - WARNING: Retries, rate limiting, malformed API responses
# - ERROR: Breaking failures

# Change level to logging.WARNING for quieter output (production)
# Change level to logging.DEBUG for maximum verbosity (troubleshooting)

# Create Pyke instance and make requests
api = Pyke(API_KEY)

# Make a request - you'll see INFO logs showing the URL and rate limit status
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")

# Other useful logging configurations:

# Completely silent (no logs from pyke):
# logging.getLogger('pyke').setLevel(logging.CRITICAL)

# Log to file instead of console:
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
#     filename="api_requests.log"
# )
```

---

## Features

- Provides a simple, pythonic interface to interact with the Riot API.
- Smart rate limiting, no wasted calls and no hitting the rate limit (configurable).
- Optimal api key usage.
- Follows Riot API endpoints and conventions closely.
- Returns Pydantic models for easy access to API data.
- Custom exceptions for error handling, e.g., rate limits.

---

## Documentation & Examples

- [Documentation](https://diodemusic.github.io/pyke/pyke.html)
- [Examples](https://github.com/diodemusic/pyke/tree/master/examples)

---

## Contact me

If you run into issues, or just have a question/need help, you can hit me up on discord.
my username is `.irm`

enjoy :)
"""

from . import endpoints, enums, exceptions, models
from .__version__ import __author__, __title__, __version__
from .enums.continent import Continent
from .enums.division import Division
from .enums.level import Level
from .enums.queue import Queue
from .enums.region import Region
from .enums.tier import Tier
from .enums.type import Type
from .main import Pyke

__all__ = [
    "exceptions",
    "Continent",
    "Division",
    "Level",
    "Queue",
    "Region",
    "Tier",
    "Type",
    "Pyke",
    "__author__",
    "__title__",
    "__version__",
    "endpoints",
    "enums",
    "models",
]
