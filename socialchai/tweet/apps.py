from django.apps import AppConfig


class TweetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tweet'

    def ready(self):
        import tweet.signals  # 👈 this line connects signals

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals