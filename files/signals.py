from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Image, Document
from common.utils import delete_s3_object, delete_file
import os
import logging

logger = logging.getLogger(__name__)

@receiver(post_delete, sender=Image)
def remove_image(sender, instance, **kwargs):
    # print('remove file receiver for {sender} fired!', flush=True)
    # print(instance, flush=True)
    logger.info(f'remove_file receiver for {sender} fired!')
    logger.info(f'Instance: {instance}')

    mode = os.getenv('MODE', 'Dev') # default to 'Dev' if MODE not found

    if mode == 'Prod':
        if instance.image:
            delete_s3_object(instance.image.url)
    else:
        if instance.image:
            delete_file(instance.image.path)

@receiver(post_delete, sender=Document)
def remove_document(sender, instance, **kwargs):
    logger.info(f'remove_file receiver for {sender} fired!')
    logger.info(f'Instance: {instance}')

    mode = os.getenv('MODE', 'Dev') # default to 'Dev' if MODE not found

    if mode == 'Prod':
        if instance.document:
            delete_s3_object(instance.document.url)
    else:
        if instance.document:
            delete_file(instance.document.path)