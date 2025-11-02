from pyke import DataDragon

# Let's create a DataDragon instance, we can pass a version if we want
# But by default the latest version will be used
# If you wish to pass a version use the following format:
# "15.21.1" (or "lolpatch_7.20" for older versions)
ddragon = DataDragon()

print(ddragon.versions.get_all_versions())
print(ddragon.champions.get_all_champions("en_GB"))
print(ddragon.champions.get_all_champions_full("en_GB"))
