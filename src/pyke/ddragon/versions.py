from .._base_data_dragon_client import _BaseDataDragonClient


class VersionsData:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    def get_all_versions(self) -> list[str]:
        """# Get all valid Data Dragon versions

        **Example:**  
            `versions = ddragon.versions.get_all_versions()`

        **Returns:**  
            `list[str]` List of versions.
        """  # fmt: skip

        return self._client._data_dragon_request("/api/versions.json")
