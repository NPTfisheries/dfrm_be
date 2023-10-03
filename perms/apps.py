# perms/apps.py
from django.apps import AppConfig
# from django.db.models.signals import post_save
# from account.models import User
# from perms.signals import assign_group

class PermsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perms'

    #def ready(self):
        #import perms.signals
        #post_save.connect(assign_group, sender=User, dispatch_uid="assign_group_unique_id")