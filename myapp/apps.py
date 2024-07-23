from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'


class YourAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from .middleware import create_user_session
        user_logged_in.connect(create_user_session)
