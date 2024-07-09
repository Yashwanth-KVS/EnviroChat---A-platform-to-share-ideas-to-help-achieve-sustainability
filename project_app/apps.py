from django.apps import AppConfig
# #
# #
# class MyAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'project_app'
#
# # # old_app/apps.py
# # from django.apps import AppConfig
# #
# # class MyappConfig(AppConfig):
# #     name = 'myapp'
# #     verbose_name = 'myapp'
#
# # Rename to new_app/apps.py
# #from django.apps import AppConfig
#
# class MyAppConfig(AppConfig):
#     name = 'project_app'
#     verbose_name = 'project_app'


# project_app/apps.py

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project_app'
    verbose_name = 'Project App'