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
        if old_instance.image1 and old_instance.image1 != instance.image1:
            instance._delete_image(old_instance.image1)
        if old_instance.image2 and old_instance.image2 != instance.image1:
            instance._delete_image(old_instance.image2)

@receiver(post_delete, sender=InvasiveSpecies)
def remove_images_on_delete(sender, instance, **kwargs):
    if instance.species_image:
        instance._delete_image(instance.species_image)
    if instance.image1:
        instance._delete_image(instance.image1)
    if instance.image2:
        instance._delete_image(instance.image2)
