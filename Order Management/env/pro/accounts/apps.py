from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    # Overriding ready function to connect to Django Signals
    def ready(self):
        import accounts.signals
