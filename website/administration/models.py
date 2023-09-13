from django.contrib.gis.db import models
from common.models import BaseModel
from account.models import User
from files.models import Image
from phonenumber_field.modelfields import PhoneNumberField

# abstract classes
class BaseAdminModel(models.Model):
    class Meta:
        abstract = True
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_manager")
    deputy = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_deputy")
    assistant = models.ForeignKey(User, null = True, blank=True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_assist")
    staff = models.ManyToManyField(User, blank=True,  related_name="%(app_label)s_%(class)s_staff")

class ImageFieldsModel(models.Model):
    class Meta:
        abstract = True
    img_banner = models.ForeignKey(Image, default = 1, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_banner")
    img_card = models.ForeignKey(Image, default = 2, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_card")

# model classes
class Department(BaseModel, BaseAdminModel, ImageFieldsModel):
    pass
    
class Division(BaseModel, BaseAdminModel, ImageFieldsModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_department")

class Project(BaseModel, ImageFieldsModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_department")
    project_leader = models.ManyToManyField(User, related_name="%(app_label)s_%(class)s_projct_leads")

class Subproject(BaseModel, ImageFieldsModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_project")
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_lead")

class Task(BaseModel, ImageFieldsModel):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_subprojects")
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_supervisor")

# model classes
class Facility(BaseModel, BaseAdminModel, ImageFieldsModel):

    FACILITY_TYPE = (
        ('Office', 'Office'),
        ('Hatchery', 'Hatchery'),
        ('Other', 'Other'),
     )

    facility_type = models.CharField(choices= FACILITY_TYPE)
    phone_number = PhoneNumberField(blank = True)
    street_address = models.CharField("Street Address", max_length=100)
    mailing_address = models.CharField("Mailing Address", null = True, blank = True, max_length=100)
    city = models.CharField("City", max_length=50)
    state = models.CharField("State", max_length=50)
    zipcode = models.CharField("Zip Code", max_length=5)
    coordinates = models.PointField()
    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'