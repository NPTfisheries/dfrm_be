# utils/image_processing.py
import boto3
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.base import ContentFile
import os

# def resize_image(instance, image_field, min_width, min_height):
#     if getattr(instance, image_field):
#         img_path = getattr(instance, image_field).path
#         img = PILImage.open(img_path)
#         print('common/utils/image_processing: Image successfully opened...', flush=True)

#         # if one of the dimensions matches, it doesn't need a resize.
#         if not (round(img.size[0], 0) == round(min_width, 0) or round(img.size[1], 0) == round(min_height, 0)):
#             print('common/utils/image_processing: Resizing image.', flush=True)
#             # print('common/utils/image_processing: First load size:', os.path.getsize(img_path), flush=True)
            
#             # cannot save an alpha to jpg, so we need to convert .png to rgb
#             if img.mode in ('RGBA', 'LA'):
#                 img = img.convert('RGB')
            
#             w_ratio = img.size[0] / min_width
#             h_ratio = img.size[1] / min_height
#             scale = min(1/w_ratio, 1/h_ratio)
#             # if w_ratio < h_ratio:  # use width
#             #     scale = min_width / img.size[0]
#             # else:  # use height
#             #     scale = min_height / img.size[1]
            
#             # (w,h)
#             new_dims = (int(img.size[0] * scale), int(img.size[1] * scale))
            
#             # save resized
#             img.resize(new_dims, PILImage.Resampling.LANCZOS).save(img_path)
#             print('common/utils/image_processing: Saved to', img_path, flush=True)
#             # print('common/utils/image_processing: Final Size:', os.path.getsize(img_path), flush=True)
#         else:
#             print('common/utils/image_processing: Image is proper size - skipping resize.', flush=True)

def resize_image(self):
        if self.image:
            img = PILImage.open(self.image)
            print('common/utils/image_processing: Image successfully opened...', flush=True)

            min_width = 1546.36
            min_height = 500

            # Check if resizing is needed
            if not (round(img.size[0]) == round(min_width) or round(img.size[1]) == round(min_height)):
                print('common/utils/image_processing: Resizing image.', flush=True)
                
                # Convert image mode if necessary
                if img.mode in ('RGBA', 'LA'):
                    img = img.convert('RGB')
                
                # Calculate scale
                w_ratio = img.size[0] / min_width
                h_ratio = img.size[1] / min_height
                scale = min(1/w_ratio, 1/h_ratio)
                
                # Calculate new dimensions
                new_dims = (int(img.size[0] * scale), int(img.size[1] * scale))
                
                # Resize the image
                img_resized = img.resize(new_dims, PILImage.Resampling.LANCZOS)

                # Save resized image to a BytesIO object
                img_bytes = BytesIO()
                img_resized.save(img_bytes, format='JPEG')
                img_bytes.seek(0)

                # Replace the original image with the resized image
                self.image.save(self.image.name, ContentFile(img_bytes.read()), save=False)
                print('common/utils/image_processing: Resized image set to model field.', flush=True)
            else:
                print('common/utils/image_processing: Image is proper size - skipping resize.', flush=True)