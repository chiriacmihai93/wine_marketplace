from django.apps import AppConfig
import profile.signals

class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'

    def ready(self):

#import profile.signals