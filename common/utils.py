# utils/image_processing.py
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.base import ContentFile

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
                image.save(image.name, ContentFile(img_bytes.read()), save=False)
                print('common/utils/image_processing: Resized image set to model field.', flush=True)
            else:
                print('common/utils/image_processing: Image is proper size - skipping resize.', flush=True)