# Pyke – Development Task List

---

# [x] Backwards compatibility

**Description:** Change Python version in `pyproject.toml` to the earliest possible working version of Python.

---

## [ ] Library Audit

**Description**: Review existing modules in `src/pyke` for consistency, naming, and type coverage. Identify duplicated logic, unclear class responsibilities, or missing docstrings.

---

## [ ] Consistent Error Handling System

**Description**: Define a unified `exceptions.py` that all modules use. Include typed exceptions (e.g., `RateLimitError`, `InvalidRegionError`, `UnauthorizedError`).

**Acceptance Criteria**:

- No untyped `raise Exception`.
- All client errors map to meaningful exceptions.
- Tests cover raised exceptions.

**Files to Create/Edit**:

- `src/pyke/exceptions.py`
- `tests/test_exceptions.py`

---

## [x] Rate Limit Handling Improvement

**Description**: Implement rate limit sleep and retry logic without redundant calls. Integrate internal `_handle_rate_limit(response: Response)` utility.

**Acceptance Criteria**:

- Handles 429 responses gracefully (single print per event).
- Respects Riot headers (`Retry-After`, `X-Method-Rate-Limit`).
- No duplicate URL printouts when sleeping.

**Files to Edit**:

- `src/pyke/_base_client.py`
- Add tests under `tests/test_rate_limit.py`

---

## [ ] Full Type Hint Coverage

**Description**: Add or refine Python type hints across all modules.

**Acceptance Criteria**:

- `mypy` passes with no `Any` leaks (except unavoidable external APIs).
- Include `py.typed` marker in distribution.
- CI enforces `mypy` check.

---

## [ ] Example Expansion

**Description**: Expand `examples/` to include real-world League API workflows (summoner lookup, match summary, ranked stats, etc.).

**Acceptance Criteria**:

- At least 3 runnable examples with minimal setup.
- Examples referenced in README and docs.
- Verified with valid `.env` keys.

---

## [ ] Documentation Overhaul

**Description**: Improve `README.md` and `docs/` for clarity, quick start, and developer reference.

**Acceptance Criteria**:

- “Getting Started” section includes pip install, .env setup, and sample usage.
- API Reference generated via `pdoc` with examples linked.

---

## [ ] Continuous Integration & Quality

**Description**: Implement GitHub Actions workflow `ci.yml` that includes:

- Ruff lint check
- Mypy type check
- Bandit security scan
- Pytest
- Docs build via pdoc

**Acceptance Criteria**:

- Workflow passes on main branch.
- Python version matrix: [3.9, 3.10, 3.11, 3.12, 3.13, 3.14].
- `.env` values mocked for tests.

---

## [ ] Package & Distribution Polish

**Description**: Prepare for PyPI publication.

**Acceptance Criteria**:

- `pyproject.toml` includes correct metadata.
- Version auto-incremented via Git tag.
- `README.md` renders correctly on PyPI.
- `twine check dist/*` passes.

---

## [ ] Playwright QA Screenshot Capture

**Description**: Visual test baseline for documentation or web demo.

**Acceptance Criteria**:

- Script `qa-playwright-capture.sh` exists.
- Captures screenshots of docs site.
- Outputs to `public/qa-screenshots`.

---

## Quality Requirements

- [ ] All functions typed and documented with docstrings.
- [ ] Exceptions standardized.
- [ ] No redundant API calls under rate limit.
- [ ] Test coverage ≥90%.
- [ ] CI must pass fully before merge.
- [ ] Docs build without warnings.

## Technical Notes

**Development Stack**: Python ≥3.9, pytest, mypy, ruff, pdoc
**Special Instructions**: Focus on API stability, maintainability, and developer UX.
**Timeline**: Open-ended; optimize for long-term quality.

---

## Core Design & Architecture

- [x] **Mirror Riot’s API structure** intuitively (e.g., `api.summoner.by_name(region, name)` instead of arbitrary endpoints).
- [x] **Encapsulate endpoints as modules or classes** (account, summoner, match, league, etc).
- [x] **Provide clear data models** (e.g., Pydantic models for responses — `SummonerDTO`, `MatchDTO`).
- [x] **Handle authentication** cleanly (API key via env var, config file, or parameter).
- [ ] Add **rate-limit/backoff strategy configuration** (retry counts, backoff formula, headers respect).
- [ ] Add a lightweight caching layer (optional, e.g., TTLCache or Redis adapter).
- [ ] Add DDragon support.
- [ ] Add async support.

---

## HTTP Layer & Error Handling

- [x] Automatic **retry and rate-limit handling** (429 responses, backoff, respecting headers).
- [x] Friendly **exceptions** (e.g., `RiotAPIError`, `RateLimitError`, `NotFoundError`).
- [ ] Timeout handling and connection-pool reuse (via `requests.Session` or `httpx`).
- [x] Optional detailed logging (requests + responses).
- [ ] Unit tests for retry, timeout, and backoff logic.
- [ ] Add telemetry hook or callback for debug metrics (e.g., request count, latency).

---

## Data Models (DTOs)

```python
class SummonerDTO(BaseModel):
    profile_icon_id: int
    revision_date: int
    puuid: str
    summoner_level: int
    id: Optional[str]
```

- [x] Type-safe responses.
- [x] Autocompletion in IDEs.
- [x] Built-in validation and parsing.
- [ ] Add shared base model (`RiotBaseModel`) for common config (`model_config`, alias rules, etc.).
- [x] **Hide Pydantic internals from documentation**
      → Implement automated `__pdoc__` suppression in `models/__init__.py`.

---

## Developer Experience (DX)

- [x] Intelligent autocomplete (clear method names, type hints).
- [x] Helpful docstrings.
- [x] Friendly errors (e.g., “Invalid region: must be one of EUW1, NA1, KR…”).
- [x] Toggleable logging.
- [ ] Centralized configuration class (`PykeConfig`) for log level, retry count, and API key management.
- [ ] Contextual error messages (include endpoint + parameters when raising exceptions).
- [ ] CLI tool (`pyke --summoner Faker --region KR`) for quick testing.

---

## Packaging & Distribution

- [x] Well-structured package (`src/pyke/...`).
- [x] Proper `pyproject.toml` (with metadata, classifiers, dependencies).
- [x] `README.md` with usage examples and badges.
- [x] `LICENSE` and versioning (`0.1.0` → `0.2.0`).
- [x] Built docs (using `pdoc` or `mkdocs-material`).
- [x] CI pipeline (GitHub Actions) that runs PyPI build on release.
- [ ] Add `MANIFEST.in` (if needed) to include `docs/`, examples, and metadata.
- [x] Add publishing workflow (`release.yml`) that builds & uploads to PyPI when a release is tagged.

---

## Testing

- [x] Unit tests (for each endpoint wrapper).
- [x] CI pipeline (GitHub Actions) that runs tests + lints on commit.
- [x] Coverage report (badge in README).
- [ ] Test endpoints with multiple regions/continents and multiple users.
- [ ] Mock Riot API responses using `responses` or `pytest-httpx`.
- [ ] Test `429` + `503` retry/backoff behaviour deterministically.
- [ ] Add `pytest` fixtures for API keys and fake data.
- [ ] Integration test suite that runs against the real Riot API (optional).
- [ ] Add `tox` or `nox` config for local multi-Python testing.

---

## Utilities & Enhancements

- [x] Support for both “platform” and “regional” routing values (e.g., EUW1 vs EUROPE).
- [ ] CLI examples (e.g., “Get top 5 ranked players in region”).
- [ ] Add rate-limit status helper (`client.remaining_requests` etc).
- [ ] Simple caching decorator for frequent endpoints.

---

## Documentation

- [x] High-level overview: what it is, how to install, quickstart.
- [x] Endpoint examples for all major APIs.
- [x] API reference (autogenerated with `pdoc` or `mkdocs`).
- [x] **Fix Pydantic boilerplate in docs** → implement the `models/__init__.py` automation.
- [ ] Add top-level `src/pyke/__init__.py` docstring (summary of all submodules).
- [x] Add README docstring to `src/pyke/__init__.py` (install, usage, etc.).
- [x] Host docs via GitHub Pages (`pdoc --html --output-dir docs`).
- [ ] Generate per-module docstrings (`endpoints`, `enums`, `exceptions`, `main`, `models`).
- [ ] Add code examples to docstrings using triple-quoted code blocks.

---

## Branding & Presentation

- [x] Nice README with badges (PyPI version, build, docs, license).
- [x] Logo or banner.
- [x] Clear tagline.
- [ ] Example image (like “fetch summoner rank in 3 lines”).
- [ ] Add animated GIF demo in README (optional).
- [ ] Add social preview (banner in `.github/` folder).

---

## Optional Advanced Features

- [ ] Auto-discovery of endpoints (fetch from Riot’s OpenAPI spec).
- [ ] Async version of client (using `httpx.AsyncClient`).
- [ ] Rate-limit sharing across clients (thread-safe global bucket).
- [ ] Endpoint usage analytics (log which endpoints are most hit).
- [ ] Built-in caching layer (with expiration, e.g., `diskcache`).

---

## Continuous Integration & Quality

- [x] Add GitHub Action workflow (`ci.yml`) with:
  - [x] `black` lint check
  - [x] `mypy` type check
  - [x] `bandit` security scan
  - [x] `pytest` for tests
  - [x] `pdoc` doc build and artifact upload
- [x] Add dependabot to repo.
- [ ] Add badges to README: `Build`, `Docs`, `Coverage`, `Code Quality`.
- [ ] Add pre-commit hooks for `ruff`, `black`, and `isort`.

---

## Code Quality & Static Analysis

- [ ] Enforce code style: `ruff`, `black`, `isort`.
- [ ] Type checking with `mypy` (include `py.typed` marker in package).
- [ ] Security scanning with `bandit`.
- [ ] Optional: complexity check (`radon`) and formatting check (`docformatter`).
- [ ] Periodic dependency review (`pip-audit` or `safety`).

---

## Contributor Experience

- [ ] Add `CONTRIBUTING.md` (setup, lint/test commands, release steps).
- [ ] Add `CODE_OF_CONDUCT.md`.
- [ ] Template issue and PR forms under `.github/`.
- [ ] “Good first issue” labels for contributors.
- [ ] Add changelog (`CHANGELOG.md`) and semantic versioning notes.

---
