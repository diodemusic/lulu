# pyke

[![Upload Python Package](https://github.com/diodemusic/pyke/actions/workflows/python-publish.yml/badge.svg?event=release)](https://github.com/diodemusic/pyke/actions/workflows/python-publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/pyke-lol)](https://pypi.org/project/pyke-lol/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/diodemusic/pyke/blob/main/LICENCE.txt)
![Coverage](https://img.shields.io/badge/Coverage-94%25-brightgreen.svg)

**pyke** is an opinionated, simple-by-design Riot API wrapper specifically for League of Legends.

![Pyke Logo](https://github.com/diodemusic/pyke/blob/main/assets/logo.png?raw=true)

## Installation

Install the latest version directly from PyPI:

```bash
pip install pyke-lol
```

> **Note:** You need Python 3.13+ to use pyke.

## Features

- Provides a simple, pythonic interface to interact with the Riot API.
- Follows Riot API endpoints and conventions closely.
- Returns Pydantic models for easy access to API data.
- Custom exceptions for error handling, e.g., rate limits.

## Documentation & Examples

I am currently working on adding documentation

- [Documentation (WIP)](/)
- [Examples](https://github.com/diodemusic/pyke/tree/master/examples)

## Example Usage

```py
from pyke import Pyke

# We always initialize the API like this
# We can explicitly disable url logging, by default pyke will log all url calls
api = Pyke(API_KEY, log_url=False)

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
except exceptions.RateLimitExceeded as e:
    print(e)  # Output: Rate limit exceeded (Error Code: 429)
    quit()

# Members can be accessed with dot notation just like before
print(f"PUUID: {region.puuid}")
print(f"Game: {region.game}")
print(f"Region: {region.region}")
```

enjoy :)
