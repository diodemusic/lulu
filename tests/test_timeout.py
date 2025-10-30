from unittest.mock import patch

import pytest
import requests

from pyke import Continent, Pyke, exceptions


def test_timeout_raises_custom_exception():
    api = Pyke("fake-api-key")

    with patch.object(api.account._client.session, "get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout()

        with pytest.raises(exceptions.RequestTimeout) as exc_info:
            api.account.by_riot_id(Continent.EUROPE, "test", "000")

        assert "Request timed out after 60 seconds" in str(exc_info.value)
        assert exc_info.value.error_code == 408
