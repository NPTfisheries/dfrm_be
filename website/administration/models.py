from django.db import models
from django.template.defaultfilters import slugify
from account.models import User
from PIL import Image
   
class BaseModel(models.Model):

    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_creator")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_editor")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk: # if self.pk is blank
            self.slug = slugify(self.name)
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name
    
class BaseAdminModel(models.Model):
    class Meta:
        abstract = True
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_manager")
    deputy = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_deputy")
    assistant = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_assist")
    staff = models.ManyToManyField(User, related_name="%(app_label)s_%(class)s_staff")

# class ImageFieldsModel(models.Model):
#     class Meta:
#         abstract = True
#     img_banner = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_banner")
#     img_card = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_card")

class Department(BaseModel, BaseAdminModel):
    pass
    
class Division(BaseModel, BaseAdminModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_department")

class Project(BaseModel):
    project_leader = models.ManyToManyField(User, related_name="%(app_label)s_%(class)s_projct_leads")

class Subproject(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_project")
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_lead")

class Task(BaseModel):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_subprojects")
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_supervisor")

# class Image(models.Model):
#     class Meta:
#         abstract = True

#     img_banner = models.ImageField(upload_to="images/banner/", default='images/banner_default.JPG')
#     img_card = models.ImageField(upload_to="images/card/", default='images/card_default.JPG')

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         img_b = Image.open(self.img_banner.path)
#         img_c = Image.open(self.img_card.path)

#         if img_b.height > 800 or img_b.width > 1200:  #3:2 aspect ratio
#             output_size = (1200, 800)
#             img_b.thumbnail(output_size)
#             img_b.save(self.img_banner.path)

#         if img_c.height > 267 or img_c.width > 400: #3:2 aspect ratio
#             output_size = (300, 300)
#             img_c.thumbnail(output_size)
#             img_c.save(self.img_card.path)