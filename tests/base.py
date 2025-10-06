import pytest
import lulu


@pytest.fixture(scope="session")
def api_client():
    """Initializes the API wrapper for the test session."""
    # lu = Lulu("API_KEY")

    # CONTINENT = Continent.europe.value

    # # Returns AccountDTO {puuid: str, gameName: str?, tagLine: str?}
    # account = lu.account.by_riot_id(CONTINENT, "game_name", "tag_line")

    # print(f"Riot ID: {account.game_name}#{account.tag_line}")
    # print(f"PUUID: {account.puuid}")any necessary arguments
    # return client

    r = lulu.say_hi()
    assert r == "hi"
