# Pyke – Development TODO

---

### Missing Implementation

- [ ] **Uncomment spectator tests** - `test_spectator.py` has all tests commented out (zero test coverage)

---

## High Priority Improvements

### Error Handling & Reliability

- [ ] **Replace print() with logging** - `_base_client.py` (lines 50, 59, 81, 103, 138, 147) - Use `logging` module instead of print statements

### Resource Management

- [ ] **Add context manager support** - Implement `__enter__`/`__exit__` on `Pyke` class to properly close `requests.Session()`

### Input Validation

- [ ] **Add parameter validation** - Validate inputs before API calls:
  - `count` within 0-100 range
  - `page` is positive integer
  - PUUID format validation (78 characters)
  - champion_id is positive integer

### Code Quality

- [ ] **Use list comprehensions** - Replace verbose for-loops with Pythonic list comprehensions throughout endpoints (8+ occurrences in league.py, champion_mastery.py, clash.py, lol_challenges.py)
- [ ] **Standardize docstring format** - Remove `#` prefix, consistent spacing and code block styles across all endpoints
- [ ] **Fix exception instantiation pattern** - `_base_client.py:31-42` - Store exception classes, not instances in registry dict

---

## Testing Improvements

- [ ] **Add mock tests** - Use `responses` or `pytest-httpx` to mock Riot API responses (all tests currently hit real API - slow, rate-limited, and can't test errors)
- [ ] **Test error conditions** - Mock 404, 429, 500, 503 responses to test exception handling
- [ ] **Improve test assertions** - Validate actual data (e.g., `result.puuid == TEST_PUUID`, `result.summoner_level > 0`), not just `isinstance()` checks
- [ ] **Test retry/backoff logic** - Deterministic tests for 429 handling
- [ ] **Add pytest fixtures** - Fixtures for API keys and common test data
- [ ] **Add tox/nox config** - Local multi-Python version testing
- [ ] **Test rate limiting logic** - Verify smart rate limiting calculations work correctly
- [ ] **Test edge cases** - Empty lists, None values, malformed JSON responses

---

## Core Features

### API Improvements

- [ ] **Add async support** - Create `AsyncPyke` class using `httpx.AsyncClient`
- [ ] **DDragon support** - Add static data endpoints (champions, items, etc.)
- [ ] **Caching layer** - Optional TTL cache for frequent endpoints (summoner, champion data)
- [ ] **Rate limit status helper** - Expose `client.remaining_requests` property
- [ ] **Retry configuration** - Expose `max_retries` as configurable parameter

### Developer Experience

- [ ] **Centralized config class** - `PykeConfig` for log level, retries, API key
- [ ] **Contextual error messages** - Include endpoint + params in exceptions
- [ ] **CLI tool** - `pyke --summoner Faker --region KR` for quick testing
- [ ] **Complete Queue enum** - Add ARAM, normals, and other queue types

---

## Documentation

- [ ] **Add error handling examples** - All endpoint docstrings only show happy path, add try/except examples with `exceptions.DataNotFound` etc.
- [ ] **Fix league_exp docstring** - `league_exp.py:31` - Says "Defaults to 1" but parameter is `None`, update to match actual behavior
- [ ] **Add code examples to docstrings** - More comprehensive usage examples
- [ ] **Add CONTRIBUTING.md** - Setup instructions, lint/test commands, release process
- [ ] **Add CHANGELOG.md** - Track version history and breaking changes
- [ ] **Generate per-module docstrings** - Better documentation for endpoints, enums, exceptions

---

## Polish

### Code Quality

- [ ] **Add py.typed marker** - Include in package for mypy support
- [ ] **Add pre-commit hooks** - For ruff, black, isort
- [ ] **Enforce code style** - Consistent use of ruff, black, isort
- [ ] **Periodic dependency audit** - Use pip-audit or safety
- [ ] **Add README badges** - Build status, docs, coverage, code quality
- [ ] **Improve API key validation** - `_base_client.py:24-25` - Only checks if None, should validate format/length (Riot keys are ~40 chars)

### Packaging

- [ ] **Add MANIFEST.in** - Include docs/ and examples/ in distribution
- [ ] **Fix schema generation path** - Use `__file__` for relative paths in `get_schema_json.py`
- [ ] **Version schema source** - Pin or host OpenAPI schema to avoid breaking changes

### Presentation

- [ ] **Add demo GIF** - Animated example in README
- [ ] **Add social preview** - Banner in `.github/` for social media
- [ ] **Example screenshots** - Visual guide for "fetch summoner rank in 3 lines"

---

## Future/Optional Features

- [ ] **Auto-discovery of endpoints** - Fetch from Riot's OpenAPI spec dynamically
- [ ] **Rate-limit sharing** - Thread-safe global rate limit bucket across clients
- [ ] **Endpoint usage analytics** - Track which endpoints are most frequently used
- [ ] **Advanced caching** - Redis adapter or diskcache with expiration
- [ ] **Telemetry hooks** - Callbacks for debug metrics (request count, latency)
- [ ] **Playwright QA screenshots** - Visual regression testing for docs

---
