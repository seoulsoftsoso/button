from django.apps import AppConfig
from . import mongo_updates

class YourAppConfig(AppConfig):
    name = 'landingPage'

    def ready(self):
        mongo_updates.listen_to_changes()

class LandingpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landingPage'
