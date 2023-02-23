from django.apps import AppConfig

class ResellConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sell'

    def ready(self):
        import sell.signals