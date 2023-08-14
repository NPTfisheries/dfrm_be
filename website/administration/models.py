from django.db import models
from common.models import BaseModel
from account.models import User
from files.models import Image

# abstract classes
class BaseAdminModel(models.Model):
    class Meta:
        abstract = True
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_manager")
    deputy = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_deputy")
    assistant = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_assist")
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
    project_leader = models.ManyToManyField(User, related_name="%(app_label)s_%(class)s_projct_leads")

class Subproject(BaseModel, ImageFieldsModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_project")
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_lead")

class Task(BaseModel, ImageFieldsModel):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_subprojects")
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_supervisor")