from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Image, Document
from common.utils import delete_s3_object, delete_file
import os
import logging

logger = logging.getLogger(__name__)

@receiver(post_delete, sender=Image)
def remove_image(sender, instance, **kwargs):
    logger.info(f'remove_file receiver for {sender} fired!')
    logger.info(f'Instance: {instance}')

    mode = os.getenv('MODE') 

    if mode == 'Prod':
        if instance.image:
            delete_s3_object(object_key=instance.image.url)
    else:
        if instance.image:
            delete_file(file_path=instance.image.path)

@receiver(post_delete, sender=Document)
def remove_document(sender, instance, **kwargs):
    logger.info(f'remove_file receiver for {sender} fired!')
    logger.info(f'Instance: {instance}')

    mode = os.getenv('MODE')

    if mode == 'Prod':
        if instance.document:
            delete_s3_object(object_key=instance.document.url)
    else:
        if instance.document:
            delete_file(file_path=instance.document.path)