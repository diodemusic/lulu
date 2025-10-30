# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Fixed

### Removed

### Deprecated

### Security

---

## [1.4.1]

### Added

- Initial changelog setup

### Changed

- Filter None params explicitly in `match.py:52-59`
- Changed ValueError to JSONDecodeError in `_base_client.py:109`

### Fixed

- Fixed type annotation mismatch in `clash.py:97,106`
- Fixed return type in match endpoint `match.py:64`
- Fixed type coercion in `champion_mastery.py:106`
- Fixed mutable default arguments in `base_client.py:158,164`
- Fixed league_exp parameter name in `league_exp.py:38`
- Fixed region enum case consistency in `region.py:10`
- Fixed fragile header parsing in `_base_client.py:44-84`

### Removed

- Removed dead code in `clash.py:91`
- Removed retry on 502 in `_base_client.py:145`

---

## Category Guidelines:

- **Added**: New features, endpoints, or functionality
- **Changed**: Changes to existing functionality (breaking or non-breaking)
- **Fixed**: Bug fixes, type corrections, parameter fixes
- **Removed**: Removed features, dead code removal
- **Deprecated**: Features marked for removal in future versions
- **Security**: Security fixes or improvements

## Semantic Versioning Quick Reference:

- **MAJOR** (1.0.0 → 2.0.0): Breaking changes
- **MINOR** (1.0.0 → 1.1.0): New features (backwards compatible)
- **PATCH** (1.0.0 → 1.0.1): Bug fixes (backwards compatible)
