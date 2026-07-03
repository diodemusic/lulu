import pytest
from httpx import Response
from respx import MockRouter

import pyke
from pyke import Continent, Pyke, exceptions

BASE = "https://europe.api.riotgames.com"
PUUID = "a" * 78


@pytest.mark.asyncio
async def test_rate_limit_information(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/riot/account/v1/accounts/by-puuid/{PUUID}").mock(
        return_value=Response(
            200,
            json={"puuid": PUUID, "gameName": "saves", "tagLine": "000"},
            headers=[
                ("x-app-rate-limit", "100:120,20:1"),
                ("x-app-rate-limit-count", "1:120,1:1"),
                ("x-method-rate-limit", "1000:60"),
                ("x-method-rate-limit-count", "1:60"),
                ("x-rate-limit-type", "application"),
            ],
        )
    )

    await pyke_client.account.by_puuid(Continent.EUROPE, PUUID)

    assert isinstance(pyke_client.rate_limit.app_limit, str)
    assert pyke_client.rate_limit.app_limit == "100:120,20:1"

    assert isinstance(pyke_client.rate_limit.app_count, str)
    assert pyke_client.rate_limit.app_count == "1:120,1:1"

    assert isinstance(pyke_client.rate_limit.method_limit, str)
    assert pyke_client.rate_limit.method_limit == "1000:60"

    assert isinstance(pyke_client.rate_limit.method_count, str)
    assert pyke_client.rate_limit.method_count == "1:60"
