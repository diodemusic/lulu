from pyke import Region

from .._base_client import _BaseApiClient
from .._models.status_v4 import PlatformDataDto


class StatusEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def platform_data(self, region: Region) -> PlatformDataDto:
        """# Get League of Legends status for the given platform

        **Args:**  
            `region (Region):` Region to execute against (pyke._enums.region.Region).  

        **Returns:**  
            `PlatformDataDto:` pyke._models.status_v4.PlatformDataDto
        """  # fmt: skip

        path = "/lol/status/v4/platform-data"
        data = self._client._region_request(region=region, path=path)

        return PlatformDataDto(**data)
