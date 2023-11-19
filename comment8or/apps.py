from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MessageboardAdminConfig(AdminConfig):
    default_site = 'admin.Comment8orAdminSite'


class MessageboardConfig(AppConfig):
    name = 'messageboard'
