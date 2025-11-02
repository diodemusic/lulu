# Pyke – Development TODO

---

## Core Features

### Data Dragon support

- Added get_all_feats endpoint in `ddragon/feats.py`
- Added get_all_item_modifiers endpoint in `ddragon/item_modifiers.py`
- Added get_all_item endpoint in `ddragon/item.py`
- Added get_all_language endpoint in `ddragon/language.py`
- Added get_all_map endpoint in `ddragon/map.py`
- Added get_all_mission assets endpoint in `ddragon/mission.py`
- Added get_all_profile_icon endpoint in `ddragon/profile_icon.py`
- Added get_all_runes_reforged endpoint in `ddragon/runes_reforged.py`
- Added get_all_spell_buffs endpoint in `ddragon/spell_buffs.py`
- Added get_all_sticker endpoint in `ddragon/sticker.py`
- Added get_all_summoner endpoint in `ddragon/summoner.py`

### API Improvements

- Add async support - Create `AsyncPyke` class using `httpx.AsyncClient`
- DDragon support - Add static data endpoints (champions, items, etc.)

### Developer Experience

- Contextual error messages - Include endpoint + params in exceptions
- Complete Queue enum - Add ARAM, normals, and other queue types

---

## Documentation

- Add error handling examples - All endpoint docstrings only show happy path, add try/except examples with `exceptions.DataNotFound` etc.
- Fix league_exp docstring - `league_exp.py:31` - Says "Defaults to 1" but parameter is `None`, update to match actual behavior
- Generate per-module docstrings - Better documentation for endpoints, enums, exceptions

---

## Polish

### Code Quality

- Add pre-commit hooks - For ruff, black, isort
- Periodic dependency audit - Use pip-audit or safety
- Add README badges - Build status, docs, coverage, code quality
- Improve API key validation - `_base_client.py:24-25` - Only checks if None, should validate format/length (Riot keys are ~40 chars)

### Packaging

- Add MANIFEST.in - Include docs/ and examples/ in distribution
- Fix schema generation path - Use `__file__` for relative paths in `get_schema_json.py`
- Version schema source - Pin or host OpenAPI schema to avoid breaking changes

### Presentation

- Add demo GIF - Animated example in README
- Add social preview - Banner in `.github/` for social media
- Example screenshots - Visual guide for "fetch summoner rank in 3 lines"

---

## Future/Optional Features

- Auto-discovery of endpoints - Fetch from Riot's OpenAPI spec dynamically
- Rate-limit sharing - Thread-safe global rate limit bucket across clients
- Endpoint usage analytics - Track which endpoints are most frequently used
- Playwright QA screenshots - Visual regression testing for docs

---
