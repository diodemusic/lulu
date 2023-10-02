# Lulu
An API wrapper for the Riot API.

### To do
- [ ] Add setup.py file.
- [ ] Provide documentation.
- [ ] Fix spectator tests to get params from .env file.
- [ ] Finish Turning everything into objects, no dicts.
- [ ] Optimise rate limiting, never hit a 429 and store some kind of token bucket.
- [ ] Add handling for service 429's, since it's using a header that doesn't exist on those it's going to hit a TypeError on the int conversion.
- [ ] Add SEA as a continent.
- [ ] Finish CLASH-V1.


### Completed ✓
- [x] Split public functions and private utils into seperate files.
- [x] Impliment caching.
- [x] Add unit tests.
- [x] Split up functionality into multiple files, change naming convention (match_by_puuid -> match.by_puuid).
- [x] Make region.py, continent.py etc..., dont use enums just use vars that hold strings, have all functions take strings instead of enums.
- [x] Remove ACCOUNT-V1 in favour of SUMMONER-V4.
- [x] Add logic to set api key once and forget instead of having to pass the key to every function on use.
- [x] Add settings logic, use this to change caching time to live or disable it all together.
