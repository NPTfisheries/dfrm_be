from django.db import models
from common.models import MetaModel, BaseModel
# from PIL import Image as PILimage  # Image conflict avoidance.
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import User
from django.template.defaultfilters import slugify
from common.utils import resize_image
import os

class Image(BaseModel):
    photographer = models.CharField(max_length=50)
    photo_date = models.DateField()
    source = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/uploaded/", default='images/default.JPG') #default='images/card_default.JPG'

    def save(self, *args, **kwargs):
        # Rename the file before saving, if not .jpg
        if not self.image.name.endswith('.jpg'):
            # print('files/models: renaming image.', flush=True)
            base, ext = os.path.splitext(self.image.name)
            self.image.name = base + '.jpg'

        # super(Image, self).save(*args, **kwargs)
        super().save(*args, **kwargs)

@receiver(post_save, sender=Image)
def resize_image_signal(sender, instance, **kwargs):
    resize_image(instance, 'image', min_width=1546.36, min_height=500)


class Document(MetaModel):

    DOCUMENT_TYPE = (
		("Annual Report","Annual Report"),
		("Journal Article","Journal Article"),
		("Technical Memo","Technical Memo"),
		("Presentation Slides","Presentation Slides"),
		("Other","Other")
	)
         
    document = models.FileField(upload_to='documents/', blank=True, max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    primary_author = models.CharField(max_length=50)
    employee_authors = models.ManyToManyField(User, related_name="%(app_label)s_%(class)s_employee_authors", blank=True)
    publish_date = models.DateField()
    document_type = models.CharField(choices = DOCUMENT_TYPE, max_length=50)
    citation = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=100, null=True, blank=True)
