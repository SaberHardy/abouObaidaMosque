from django.apps import AppConfig


class AppabuobaidaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appAbuObaida'

    def ready(self):
        import appAbuObaida.signals
