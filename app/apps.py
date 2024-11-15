from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

# app/apps.py

from django.apps import AppConfig

class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        # Start the reminder task when the app is ready
        from . import views
