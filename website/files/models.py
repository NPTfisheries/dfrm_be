from django.db import models
from common.models import BaseModel
from PIL import Image

# Create your models here.

class Image(BaseModel):
    photographer = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/uploaded/", default='images/banner_default.JPG') #default='images/card_default.JPG'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img_b = Image.open(self.img_banner.path)
    #     img_c = Image.open(self.img_card.path)

    #     if img_b.height > 800 or img_b.width > 1200:  #3:2 aspect ratio
    #         output_size = (1200, 800)
    #         img_b.thumbnail(output_size)
    #         img_b.save(self.img_banner.path)

    #     if img_c.height > 267 or img_c.width > 400: #3:2 aspect ratio
    #         output_size = (300, 300)
    #         img_c.thumbnail(output_size)
    #         img_c.save(self.img_card.path)