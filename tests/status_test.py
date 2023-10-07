import lulu
from dotenv import load_dotenv
import os
import utils


load_dotenv()
key = os.getenv("KEY")
region = lulu.region.euw


settings = lulu.settings.SettingsManager()
settings.set_api_key(key)
settings.set_cache_enabled(False)


def test_platform_data():
    instance = lulu.status.platform_data(region)

    assert type(instance) == utils.classes.PlatformData
    assert type(instance.platform_id) == str
    assert type(instance.name) == str
    assert type(instance.locales) == list

    for locale in instance.locales:
        assert type(locale) == str

    assert type(instance.maintenances) == list

    for maintenence in instance.maintenances:
        assert type(maintenence) == utils.classes.Status
        assert type(maintenence.status_id) == int
        assert type(maintenence.maintenance_status) == str
        assert type(maintenence.incident_severity) == str
        assert type(maintenence.titles) == list

        for title in maintenence.titles:
            assert type(title) == utils.classes.Content
            assert type(title.locale) == str
            assert type(title.content) == str

        assert type(maintenence.updates) == list

        for update in maintenence.updates:
            assert type(update) == utils.classes.Update
            assert type(update.update_id) == int
            assert type(update.author) == str
            assert type(update.publish) == bool
            assert type(update.publish_locations) == list

            for publish_location in update.publish_locations:
                assert type(publish_location) == str

            assert type(update.translations) == list

            for translation in maintenence.translations:
                assert type(translation) == utils.classes.Content
                assert type(translation.locale) == str
                assert type(translation.content) == str

            assert type(update.created_at) == str
            assert type(update.updated_at) == str

        assert type(maintenence.created_at) == str
        assert type(maintenence.archive_at) == str
        assert type(maintenence.updated_at) == str
        assert type(maintenence.platforms) == list

        for platform in maintenence.platforms:
            assert type(platform) == str

    assert type(instance.incidents) == list

    for incident in instance.incidents:
        assert type(incident) == utils.classes.Status
        assert type(incident.status_id) == int
        assert type(incident.maintenance_status) == str
        assert type(incident.incident_severity) == str
        assert type(incident.titles) == list

        for title in incident.titles:
            assert type(title) == utils.classes.Content
            assert type(title.locale) == str
            assert type(title.content) == str

        assert type(incident.updates) == list

        for update in incident.updates:
            assert type(update) == utils.classes.Update
            assert type(update.update_id) == int
            assert type(update.author) == str
            assert type(update.publish) == bool
            assert type(update.publish_locations) == list

            for publish_location in update.publish_locations:
                assert type(publish_location) == str

            assert type(update.translations) == list

            for translation in incident.translations:
                assert type(translation) == utils.classes.Content
                assert type(translation.locale) == str
                assert type(translation.content) == str

            assert type(update.created_at) == str
            assert type(update.updated_at) == str

        assert type(incident.created_at) == str
        assert type(incident.archive_at) == str
        assert type(incident.updated_at) == str
        assert type(incident.platforms) == list

        for platform in incident.platforms:
            assert type(platform) == str
