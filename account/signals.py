#accounts/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, Profile
import os
from common.utils import delete_file, delete_s3_object

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# photo update signals
@receiver(pre_save, sender=Profile)
def backup_old_photo(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_photo = Profile.objects.get(pk=instance.pk).photo
            if old_photo and old_photo != instance.photo:
                instance._old_photo = old_photo
        except Profile.DoesNotExist:
            pass

@receiver(post_save, sender=Profile)
def remove_old_photo(sender, instance, **kwargs):
    mode = os.getenv('MODE') 

    if hasattr(instance, '_old_photo'):
        if instance._old_photo.name != 'images/profile/profile_default.jpg':
            if mode == 'Prod':
                if instance.photo:
                    delete_s3_object(object_key=f'media/{instance._old_photo.name}')
            else:
                if instance.photo:
                    delete_file(file_path=instance._old_photo.path) # dev

        del instance._old_photo