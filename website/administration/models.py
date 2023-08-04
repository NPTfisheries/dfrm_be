from django.db import models
from account.models import User
from PIL import Image

class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ['name']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.banner.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.banner.path)

    def __str__(self):
        return self.name

class Department(BaseModel):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'dept_manager', verbose_name = "Department Manager")
    deputy_manager = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE, related_name = 'dept_deputy', verbose_name = "Deputy Manager")
    administrative_assistant = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name = 'dept_assist', verbose_name = "Administrative Assistant")
    #managers = models.ManyToManyField(User, verbose_name="Management Staff", blank=True)
    name = models.CharField("Department Name", max_length=300)
    description = models.TextField("Department Desecription")
    banner = models.ImageField("Department Banner", upload_to='images/department/', default='images/wallowalake.JPG')

class Division(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Division Department")
    director = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'div_director', verbose_name="Division Director")
    deputy_director = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE, related_name = 'div_deputy', verbose_name="Deputy Division Director")
    administrative_assistant = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name = 'div_assist', verbose_name = "Administrative Assistant")
    #managers = models.ManyToManyField(User, verbose_name="Managers", blank=True)
    name = models.CharField("Division Name", max_length=300)
    description = models.TextField("Division Desecription")
    banner = models.ImageField("Division Banner", upload_to='images/division/', default='images/wallowalake.JPG')

class Project(BaseModel):
    project_leader = models.ManyToManyField(User, verbose_name="Project Leader")
    name = models.CharField("Project Name", max_length=300)
    description = models.TextField("Project Description")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Project Created")
    is_active = models.BooleanField("Active Project (check for yes)", default=True)
    banner = models.ImageField("Project Banner", upload_to='images/project/', default='images/wallowalake.JPG')