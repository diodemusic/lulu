# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial changelog setup

### Changed

### Fixed

- Fixed type annotation mismatch `clash.py:97,106`
- Fixed return type in match endpoint `match.py:64`
- Fixed type coercion in `champion_mastery.py:106`
- Fixed mutable default arguments in `base_client.py:158,164`
- Fixed league_exp parameter name in `league_exp.py:38`

### Removed

- Removed dead code in `clash.py:91`
- Removed retry on 502 in `_base_client.py:145`

### Deprecated

### Security

---

## How to Use This Changelog

When you complete a TODO item, move it to the appropriate section under **[Unreleased]** using this format:

### Category Guidelines:

- **Added**: New features, endpoints, or functionality
- **Changed**: Changes to existing functionality (breaking or non-breaking)
- **Fixed**: Bug fixes, type corrections, parameter fixes
- **Removed**: Removed features, dead code removal
- **Deprecated**: Features marked for removal in future versions
- **Security**: Security fixes or improvements

### Entry Format:

```markdown
- Brief description of change - `file.py:line` if relevant (#PR-number if applicable)
```

### Example Workflow:

**Before (TODO.md):**

```
- [x] Fix type annotation mismatch in clash - `clash.py:97,106`
```

**After (CHANGELOG.md under [Unreleased] > Fixed):**

```
- Fixed type annotation mismatch in clash endpoint - `clash.py:97,106`
- Fixed typo in docstring "Tournement" → "Tournament" - `clash.py:97`
```

### Releasing a Version:

When ready to release, replace `[Unreleased]` with a version number and date:

```markdown
## [Unreleased]

### Added

### Changed

---

## [0.2.0] - 2025-10-29

### Added

- Added context manager support for Pyke class
- Added configurable timeout parameter

### Fixed

- Fixed infinite retry loop on 502 errors with exponential backoff - `_base_client.py:116`
- Fixed mutable default arguments in \_base_client - `_base_client.py:162,168`
```

### Tips:

1. **Be specific**: Instead of "Fixed bug", write "Fixed infinite retry loop on 502 errors"
2. **Reference locations**: Include file paths for code changes
3. **Group related changes**: Multiple fixes to the same file can be one bullet
4. **Keep it user-focused**: Write for people reading release notes, not just developers

### Semantic Versioning Quick Reference:

- **MAJOR** (1.0.0 → 2.0.0): Breaking changes
- **MINOR** (1.0.0 → 1.1.0): New features (backwards compatible)
- **PATCH** (1.0.0 → 1.0.1): Bug fixes (backwards compatible)
