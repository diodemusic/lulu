import pytest

from lulu import Lulu


@pytest.fixture
def lu() -> Lulu:
    """Initializes the API wrapper for the test session."""
    lu = Lulu("api_key_abc123")

    return lu
