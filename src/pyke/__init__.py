"""# pyke

[![PyPI - Version](https://img.shields.io/pypi/v/pyke-lol)](https://pypi.org/project/pyke-lol/)
[![Documentation](https://img.shields.io/badge/Documentation-blue)](https://diodemusic.github.io/pyke/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyke-lol)](https://pypi.org/project/pyke-lol/)
![Coverage](https://img.shields.io/badge/Coverage-94%25-brightgreen.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/diodemusic/pyke/blob/main/LICENCE.txt)

**pyke** is a production-ready Riot API wrapper with intelligent rate limiting and robust error handling, specifically designed for League of Legends.

## Key Features

- **Smart Rate Limiting** - Dynamic request throttling based on API headers to maximize throughput while preventing 429 errors
- **Resilient Retry Logic** - Retry strategies for rate limits and server errors with intelligent exponential backoff
- **Type-Safe** - Full Pydantic model support with comprehensive type hints for autocompletion and validation
- **Pythonic API** - Clean, intuitive interface that mirrors Riot's API structure exactly
- **Production Logging** - Standard Python logging integration with configurable levels
- **Highly Configurable** - Customize timeouts, retry limits, rate limiting behavior, and more

---

## Installation

Install the latest version directly from PyPI:

```bash
pip install pyke-lol
```

> **Note:** You need Python 3.9+ to use pyke.

---

## Quickstart

```py
from pyke import Continent, Pyke, exceptions

# Initialize the API
api = Pyke("RGAPI-...")

# Every pyke method follows the same convention as the Riot API
# For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes:
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Every response is a Pydantic model with dot notation access
print(f"Riot ID: {account.game_name}#{account.tag_line}")
print(f"PUUID: {account.puuid}")

# Pydantic models provide convenient serialization
print(account.model_dump_json())  # JSON string
print(account.model_dump())       # Python dictionary

# pyke throws typed exceptions matching Riot API error codes
try:
    region = api.account.region_by_puuid(Continent.EUROPE, account.puuid)
except exceptions.DataNotFound as e:
    print(e)  # Output: Data not found (Error Code: 404)
    quit()

print(f"PUUID: {region.puuid}")
print(f"Game: {region.game}")
print(f"Region: {region.region}")
```

---

## Configuration

pyke offers extensive configuration options for production use:

```py
from pyke import Pyke

api = Pyke(
    api_key="RGAPI-...",
    smart_rate_limiting=True,      # Enable intelligent rate limiting (default: True)
    timeout=60,                    # Request timeout in seconds (default: 60)
    max_rate_limit_retries=5,      # Max retries for 429 errors (default: 5)
    max_server_error_retries=3,    # Max retries for 502/503/504 (default: 3)
)
```

### Smart Rate Limiting

pyke's rate limiting algorithm analyzes response headers to:

- Calculate optimal wait times between requests
- Maximize throughput without hitting rate limits
- Automatically respect `Retry-After` headers on 429 responses

**Result:** Zero rate limit violations while maintaining maximum request speed.

### Intelligent Retry Logic

pyke uses **separate retry strategies** for different error types:

**Rate Limit Errors (429):**

- Independent retry counter (default: 5 attempts)
- Respects `Retry-After` header from API
- Logs retry progress: `Rate limit retries: 2/5`

**Server Errors (502/503/504):**

- Separate retry counter (default: 3 attempts)
- Error-specific exponential backoff:
  - **504 Gateway Timeout:** 10s base (10s → 20s → 40s) - longer recovery for backend timeouts
  - **502/503 Server Errors:** 5s base (5s → 10s → 20s) - faster recovery for transient issues
- Prevents infinite retry loops while maintaining resilience

---

## Logging

pyke uses Python's standard `logging` module for comprehensive diagnostics:

```py
import logging
from pyke import Pyke

# Configure logging before creating Pyke instance
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

api = Pyke("RGAPI-...")
```

### Log Levels

- **DEBUG:** Detailed diagnostic information
- **INFO:** Request URLs with rate limit tracking: `(45/100) - https://na1.api.riotgames.com/...`
- **WARNING:** Retries, rate limiting, malformed API responses
- **ERROR:** Critical failures

### Common Configurations

```py
# Production (quiet) - only warnings and errors
logging.basicConfig(level=logging.WARNING)

# Development (verbose) - see all requests
logging.basicConfig(level=logging.INFO)

# Debugging - maximum verbosity
logging.basicConfig(level=logging.DEBUG)

# Completely silent
logging.getLogger('pyke').setLevel(logging.CRITICAL)

# Log to file
logging.basicConfig(
    level=logging.INFO,
    filename="api_requests.log",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
```

---

## Advanced Features

### Type Safety with Pydantic Models

All API responses are Pydantic models with full type hints:

```py
from pyke import Pyke, Region

api = Pyke("RGAPI-...")

account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")
summoner = api.summoner.by_puuid(Region.EUW, account.puuid)

# Dot notation access with autocomplete
print(summoner.puuid)             # Type: str
print(summoner.summoner_level)    # Type: int
print(summoner.profile_icon_id)   # Type: int

# JSON serialization
json_str = summoner.model_dump_json()
dict_data = summoner.model_dump()
```

### Custom Exception Handling

pyke provides typed exceptions for all HTTP status codes:

```py
from pyke import exceptions

try:
    summoner = api.summoner.by_puuid(Region.EUW, "NonExistentPuuid")
except exceptions.DataNotFound as e:
    print(f"Not found: {e}")     # Data not found (Error Code: 404)
except exceptions.RateLimitExceeded as e:
    print(f"Rate limited: {e}")  # Rate limit exceeded after 5 retries (Error Code: 429)
except exceptions.InternalServerError as e:
    print(f"Server error: {e}")  # Internal server error (Error Code: 500)
```

**Available exceptions:**
`BadRequest` (400), `Unauthorized` (401), `Forbidden` (403), `DataNotFound` (404), `MethodNotAllowed` (405), `UnsupportedMediaType` (415), `RateLimitExceeded` (429), `InternalServerError` (500), `BadGateway` (502), `ServiceUnavailable` (503), `GatewayTimeout` (504)

### Continental vs Regional Routing

pyke automatically handles Riot's routing requirements:

```py
from pyke import Continent, Region

# Continental routing (Account-V1, Match-V5)
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Regional routing (Summoner-V4, League-V4, etc.)
summoner = api.summoner.by_puuid(Region.EUW, account.puuid)
```

**Continental Routing:**

- `AMERICAS`: NA, BR, LAN, LAS
- `ASIA`: KR, JP
- `EUROPE`: EUNE, EUW, ME1, TR, RU
- `SEA`: OCE, SG2, TW2, VN2

---

## Complete Feature List

- **Smart Rate Limiting** - Dynamic throttling based on API headers
- **Dual Retry Strategies** - Separate 429 and 50x retry logic with exponential backoff
- **Type-Safe Models** - 97 Pydantic models with full type hints
- **Production Logging** - Standard Python logging with configurable levels
- **Custom Exceptions** - 11 typed exception classes for precise error handling
- **Continental Routing** - Automatic routing for Account/Match endpoints
- **Configurable Timeouts** - Adjust request timeouts for slow endpoints
- **Mirror API Design** - Intuitive mapping to Riot's API structure
- **Pythonic Interface** - Clean, idiomatic Python code
- **94% Test Coverage** - Comprehensive integration test suite
- **Python 3.9-3.14** - Tested across 6 Python versions

---

## Documentation & Resources

- **[API Documentation](https://diodemusic.github.io/pyke/pyke.html)** - Complete API reference with examples
- **[Examples Directory](https://github.com/diodemusic/pyke/tree/master/examples)** - 15+ working examples covering all features
- **[PyPI Package](https://pypi.org/project/pyke-lol/)** - Official package distribution
- **[GitHub Repository](https://github.com/diodemusic/pyke)** - Source code and issue tracking

---

## Contributing & Support

Found a bug or have a feature request? Open an issue on [GitHub](https://github.com/diodemusic/pyke/issues).

For questions or help, reach out on Discord: `.irm`

---

## License

MIT License - see [LICENSE.txt](https://github.com/diodemusic/pyke/blob/main/LICENCE.txt) for details.

---

**Made with ❤️ for the League of Legends developer community**
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
