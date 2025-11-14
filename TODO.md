# Pyke – Development TODO

**Organized by Priority** - Work from top to bottom for maximum impact.

---

## Security & Stability (v2.2.0 - Minor Release)

**Important improvements for production reliability**

### Security

- [ ] **Use HTTPS for schema URL** - `get_schema_json.py:5` - Change to `https://www.mingweisamuel.com/...`
- [ ] **Version schema source** - Pin or host OpenAPI schema copy to avoid breaking changes
- [ ] **Add schema fallback mechanism** - If primary source fails, use backup or cached version
- [ ] **Improve API key validation** - `_base_client.py:30-31` - Validate format/length (Riot keys are ~42 chars, start with "RGAPI-")
- [ ] **Add secrets detection** - Install git-secrets or detect-secrets pre-commit hook
- [ ] **Validate DDragon responses** - Create Pydantic models for DDragon endpoints instead of `dict[str, Any]`

### Code Cleanup

- [ ] **Remove or document commented code** - `main.py:35,85` - Either delete versions endpoint code or explain why disabled
- [ ] **Fix schema generation path** - `get_schema_json.py:12` - Use `__file__` for relative paths instead of hardcoded `"./pyke/generators/schema.json"`
- [ ] **Add proper return type annotations** - `_base_data_dragon_client.py:82,89` - Replace TODO comments with actual types

---

## Documentation (v2.2.0)

**Improve developer experience and onboarding**

- [ ] **Add error handling examples** - All endpoint docstrings only show happy path, add try/except examples with `exceptions.DataNotFound` etc.
- [ ] **Fix league_exp docstring** - `league_exp.py:31` - Says "Defaults to 1" but parameter is `None`, update to match actual behavior
- [ ] **Document region enum ambiguity** - `enums/region.py:19-23` - Clarify why PH/SG/TH all map to "sg2"
- [ ] **Add architecture diagram** - Visual showing Pyke → \_BaseApiClient → endpoints flow
- [ ] **Document rate limiting behavior** - Add detailed explanation of smart rate limiting algorithm
- [ ] **Generate per-module docstrings** - Better documentation for endpoints, enums, exceptions
- [ ] **Add troubleshooting guide** - Common errors (401, 403, 404, 429) and solutions
- [ ] **Document testing requirements** - Clearly explain .env setup and test fixtures needed

---

## Testing (v2.3.0)

**Expand test coverage and CI reliability**

- [ ] **Add unit tests** - Currently only integration tests, add mocked unit tests for:
  - Rate limiting logic
  - Retry mechanisms
  - Exception handling
  - Header parsing
- [ ] **Add error condition tests** - Mock 400, 401, 403, 429, 500, 502, 503, 504 responses
- [ ] **Test timeout handling** - Verify timeout behavior works correctly
- [ ] **Add edge case tests** - Empty responses, malformed JSON, invalid headers
- [ ] **Test concurrent requests** - Verify rate limiting works with parallel requests
- [ ] **Add performance benchmarks** - Track request latency and throughput
- [ ] **Test rate limit sharing** - If implemented, verify cross-instance behavior

---

## Core Features (v2.4.0+)

**Major functionality additions**

### Async Support (v2.4.0)

- [ ] **Create AsyncPyke class** - Use `httpx.AsyncClient` for async/await support
- [ ] **Async rate limiting** - Adapt smart rate limiting for async context
- [ ] **Async retry logic** - Handle retries with `asyncio.sleep()`
- [ ] **Async endpoint classes** - Create async versions of all endpoints
- [ ] **Async tests** - Add pytest-asyncio tests
- [ ] **Async documentation** - Add examples and migration guide

### Developer Experience

- [ ] **Contextual error messages** - Include endpoint + params in exceptions (e.g., "404 on /lol/summoner/v4/summoners/by-puuid/{puuid}")
- [ ] **Complete Queue enum** - Add ARAM, normals, and other missing queue types
- [ ] **Add retry callbacks** - Allow users to hook into retry events for monitoring
- [ ] **Request logging improvements** - Structured logging with request/response correlation IDs
- [ ] **Add request hooks** - Allow middleware-like request/response processing

---

## Code Quality (Ongoing)

**Maintain high standards and prevent regressions**

- [ ] **Add pre-commit hooks** - Install and configure:
  - black (formatting)
  - ruff (linting)
  - isort (import sorting)
  - mypy (type checking)
  - bandit (security)
  - detect-secrets (secret detection)
- [ ] **Set up Dependabot** - Auto-update dependencies with security patches
- [ ] **Periodic dependency audit** - Use pip-audit or safety monthly
- [ ] **Add coverage thresholds** - Enforce 90%+ coverage in CI
- [ ] **Add mutation testing** - Use mutmut to verify test effectiveness
- [ ] **Set up SonarCloud** - Code quality and security analysis
- [ ] **Add CODEOWNERS file** - Define code review requirements

---

## Packaging & Distribution (v2.2.0+)

**Improve package quality and discoverability**

- [ ] **Add MANIFEST.in** - Include docs/ and examples/ in distribution
- [ ] **Add py.typed marker** - Signal that package includes type hints
- [ ] **Configure package metadata** - Add project URLs (docs, issues, source) to pyproject.toml
- [ ] **Add classifiers** - Improve PyPI categorization (Development Status :: 5, Typing :: Typed)
- [ ] **Set up GitHub Releases** - Auto-create releases from tags with changelog
- [ ] **Add installation verification** - Script to verify install worked correctly
- [ ] **Consider wheel optimization** - Pre-compile or optimize for faster installs

---

## Presentation (v2.2.0+)

**Marketing and user engagement**

- [ ] **Add demo GIF** - Animated example in README showing quickstart
- [ ] **Add social preview** - Banner in `.github/` for social media sharing
- [ ] **Example screenshots** - Visual guide for "fetch summoner rank in 3 lines"
- [ ] **Add more README badges** - Build status, docs, coverage, code quality, downloads
- [ ] **Create comparison table** - Compare pyke vs other Python Riot API wrappers
- [ ] **Add use case examples** - Real-world scenarios (match history analyzer, rank tracker, etc.)
- [ ] **Record demo video** - 2-3 minute walkthrough for YouTube/docs site
- [ ] **Write blog post** - "Building a production-ready API wrapper" on dev.to or Medium

---

## Advanced Features (v3.0.0+)

**Future enhancements for power users**

### Performance

- [ ] **Rate-limit sharing** - Thread-safe global rate limit bucket across Pyke instances
- [ ] **Connection pooling config** - Expose requests.Session configuration
- [ ] **Response caching** - Optional caching layer for static/semi-static data
- [ ] **Batch request optimization** - Intelligently batch compatible requests
- [ ] **Circuit breaker pattern** - Auto-disable endpoints returning consistent errors

### Observability

- [ ] **OpenTelemetry integration** - Add tracing and metrics support
- [ ] **Endpoint usage analytics** - Track which endpoints are most frequently used
- [ ] **Rate limit metrics** - Export Prometheus metrics for rate limit status
- [ ] **Request/response logging** - Structured JSON logs for analysis

### Advanced API Features

- [ ] **Automatic pagination** - Helper to auto-paginate through results
- [ ] **Data transformation pipelines** - Chain transformations on responses
- [ ] **Auto-discovery of endpoints** - Fetch endpoint definitions from Riot's OpenAPI spec dynamically

### Developer Tools

- [ ] **CLI tool** - Command-line interface for quick queries (`pyke summoner saves-000`)
- [ ] **Mock server** - Local Riot API mock for testing
- [ ] **Request recorder** - Record/replay requests for testing
- [ ] **Interactive REPL** - IPython-based interactive shell
- [ ] **VSCode extension** - Autocomplete and inline docs

---

## Quality Assurance (Ongoing)

**Maintain excellence over time**

- [ ] **Playwright QA screenshots** - Visual regression testing for docs
- [ ] **Load testing** - Verify rate limiting under high concurrency
- [ ] **Chaos engineering** - Test resilience to API failures
- [ ] **Compatibility testing** - Verify across Python 3.9-3.13
- [ ] **Memory profiling** - Ensure no leaks in long-running processes
- [ ] **Security audits** - Annual third-party security review

---

## Community & Ecosystem (Ongoing)

**Build a healthy community**

- [ ] **Create CONTRIBUTING.md** - Guide for contributors
- [ ] **Set up Discussions** - GitHub Discussions for Q&A
- [ ] **Create example projects** - Full applications using pyke
- [ ] **Integration guides** - Discord bot, web dashboard, data analysis
- [ ] **Add to Riot API Libraries list** - Submit to official Riot API docs
- [ ] **Create Discord server** - Community support and discussion
- [ ] **Monthly release cadence** - Predictable update schedule
- [ ] **Publish roadmap** - Public visibility into upcoming features

---
