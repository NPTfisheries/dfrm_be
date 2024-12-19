from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import InvasiveSpecies
from common.utils import delete_file, delete_s3_object
from django.conf import settings

@receiver(pre_save, sender=InvasiveSpecies)
def delete_old_images(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.species_image and old_instance.species_image != instance.species_image:
            instance._delete_image(old_instance.species_image)
        if old_instance.map_image and old_instance.map_image != instance.map_image:
            instance._delete_image(old_instance.map_image)

@receiver(post_delete, sender=InvasiveSpecies)
def remove_images_on_delete(sender, instance, **kwargs):
    if instance.species_image:
        instance._delete_image(instance.species_image)
    if instance.map_image:
        instance._delete_image(instance.map_image)
