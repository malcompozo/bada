from django.apps import AppConfig


class DefaultEventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'default_event'
    verbose_name = "Eventos predefinidos"
