# Lulu
An API wrapper for the Riot API.

### To do
- [ ] Add setup.py to install dependencies.
- [ ] Add logic to set api key once and forget instead of having to pass the key to every function on use.
- [ ] Provide extensive documentation.
- [ ] Make a folder for cached calls that do not need a time to live. (matches only need to be fetched once, the data is static).
- [ ] Fix spectator tests to get params from .env file.

### Completed ✓
- [x] Split public functions and private utils into seperate files.
- [x] Impliment caching.
- [x] Add unit tests.
- [x] Split up functionality into multiple files, change naming convention (match_by_puuid -> match.by_puuid).
- [x] Make region.py, continent.py etc..., dont use enums just use vars that hold strings, have all functions take strings instead of enums.
