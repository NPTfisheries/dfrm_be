# utils/image_processing.py
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.base import ContentFile

import boto3
from django.conf import settings

import environ
import os
import logging

env = environ.Env()
logger = logging.getLogger(__name__)

def resize_image(self, image_field, min_width, min_height):
        image = getattr(self, image_field)
        if image:
            img = PILImage.open(image)

            # Check if resizing is needed
            if not (round(img.size[0]) == round(min_width) or round(img.size[1]) == round(min_height)):
                print('common/utils/image_processing: Resizing image.', flush=True)
                
                # Convert image mode if necessary
                if img.mode in ('RGBA', 'LA'):
                    img = img.convert('RGB')
                
                # Calculate scale
                w_ratio = img.size[0] / min_width
                h_ratio = img.size[1] / min_height

                if w_ratio > h_ratio: 
                    scale = min_width/img.size[0]
                else:
                    scale = min_height/img.size[1]
                
                # Calculate new dimensions
                new_dims = (int(img.size[0] * scale), int(img.size[1] * scale))
                
                # Resize the image
                img_resized = img.resize(new_dims, PILImage.Resampling.LANCZOS)

                # Save resized image to a BytesIO object
                img_bytes = BytesIO()
                img_resized.save(img_bytes, format='JPEG')
                img_bytes.seek(0)

                # Replace the original image with the resized image
                image.save(image.name, ContentFile(img_bytes.read()), save=False)
                print('common/utils/image_processing: Resized image set to model field.', flush=True)
            else:
                print('common/utils/image_processing: Image is proper size - skipping resize.', flush=True)

def delete_s3_object(object_key):
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name='us-west-2',
    )
    try:
        s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=object_key)
        logger.info(f'Successfully deleted {object_key} from S3.')
        print(f'DELETE ATTEMPT S3 for object: {object_key}', flush=True)
    except s3.exceptions.NoSuchKey:
        logger.warning(f'File {object_key} not found in S3 bucket {settings.AWS_STORAGE_BUCKET_NAME}.')
    except Exception as e:
        logger.error(f'Error deleting {object_key} from S3: {e}', exc_info=True)

def delete_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            logger.info(f'Successfully deleted local file: {file_path}.')
        else:
            logger.warning(f'File {file_path} not found locally.')
    except Exception as e:
        logger.error(f'Error deleting local file {file_path}: {e}', exc_info=True)