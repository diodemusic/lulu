# from pyke import DataDragon

# from .base import TEST_REGION, ddragon


# def test_get_all_versions(ddragon: DataDragon):
#     get_all_versions = ddragon.versions.get_all_versions()

#     assert isinstance(get_all_versions, list)
#     assert len(get_all_versions) > 0

#     for version in get_all_versions:
#         assert isinstance(version, str)

#     assert get_all_versions[0] == ddragon._client.version
