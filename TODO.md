# Pyke – Development TODO

---

## Testing Improvements

- [ ] **Add mock tests** - Use `responses` or `pytest-httpx` to mock Riot API responses
- [ ] **Test error conditions** - Mock 404, 429, 500, 503 responses
- [ ] **Improve test assertions** - Validate actual data, not just response types
- [ ] **Test retry/backoff logic** - Deterministic tests for 429 and 502 handling
- [ ] **Add pytest fixtures** - Fixtures for API keys and common test data
- [ ] **Add tox/nox config** - Local multi-Python version testing

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

## Quality Standards

- All functions must have type hints and docstrings
- Test coverage must be ≥90%
- CI must pass before merging
- Docs must build without warnings
- No redundant API calls
- All exceptions must be typed

---

## Development Stack

**Languages**: Python ≥3.9
**Testing**: pytest, responses/pytest-httpx
**Linting**: ruff, black, mypy, bandit
**Docs**: pdoc
**Build**: Poetry

---
