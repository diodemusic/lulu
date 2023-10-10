# Lulu

An API wrapper for the Riot API.

## To do

- [ ] Publish to pip and provide installation instructions.
- [ ] Wait for update/maintenence/incident to test LOL-STATUS-V4
- [ ] Wait for clash to finish CLASH-V1.
- [ ] Switch to dataclasses.
- [ ] Rename pytest cases to instance.
- [ ] Add examples for every endpoint.
- [ ] Provide documentation.
- [ ] Fix spectator tests to get params from .env file.
- [ ] Add esports as a continent.

## Completed ✓

- [x] Split public functions and private utils into seperate files.
- [x] Impliment caching.
- [x] Add unit tests.
- [x] Split up functionality into multiple files, change naming convention (match_by_puuid -> match.by_puuid).
- [x] Make region.py, continent.py etc..., dont use enums just use vars that hold strings, have all functions take strings instead of enums.
- [x] Remove ACCOUNT-V1 in favour of SUMMONER-V4.
- [x] Add logic to set api key once and forget instead of having to pass the key to every function on use.
- [x] Add settings logic, use this to change caching time to live or disable it all together.
- [x] Finish Turning all endpoints into objects.
- [x] Add setup.py file.
- [x] Add SEA as a continent.
- [x] Change dataclass naming convention to reflect the API docs.
- [x] Add handling for service 429's, since it's using a header that doesn't exist on those it's going to hit a TypeError on the int conversion.
- [x] Optimise rate limiting.
