from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Image, Document
from common.utils import delete_s3_object

@receiver(post_delete, sender=Image)
def delete_image_from_s3(sender, instance, **kwargs):
    if instance.image:
        delete_s3_object(instance.image.name)

# @receiver(post_delete, sender=Document)
# def delete_profile_image_from_s3(sender, instance, **kwargs):
#     if instance.photo:
#         delete_s3_object(instance.photo.name)
