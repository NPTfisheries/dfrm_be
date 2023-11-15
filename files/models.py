from django.db import models
from common.models import MetaModel, BaseModel
from PIL import Image
from django.urls import reverse
from account.models import User

# Create your models here.

class Image(BaseModel):
    photographer = models.CharField(max_length=50)
    photo_date = models.DateField()
    source = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/uploaded/", default='images/default.JPG') #default='images/card_default.JPG'

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

class Document(MetaModel):

    DOCUMENT_TYPE = (
		("Annual Report","Annual Report"),
		("Journal Article","Journal Article"),
		("Technical Memo","Technical Memo"),
		("Presentation Slides","Presentation Slides"),
		("Other","Other")
	)
         
    document = models.FileField(upload_to='documents/', blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    primary_author = models.CharField(max_length=50)
    employee_authors = models.ManyToManyField(User, related_name="%(app_label)s_%(class)s_employee_authors", blank=True)
    publish_date = models.DateField()
    document_type = models.CharField(choices = DOCUMENT_TYPE, max_length=50)
    citation = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=100, null=True)
