from django.db import models
from account.models import User
from PIL import Image

class Department(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'dept_manager', verbose_name = "Department Manager")
    deputy_manager = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE, related_name = 'dept_deputy', verbose_name = "Deputy Manager")
    administrative_assistant = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name = 'dept_assist', verbose_name = "Administrative Assistant")
    #managers = models.ManyToManyField(User, verbose_name="Management Staff", blank=True)
    name = models.CharField("Department Name", max_length=300)
    description = models.TextField("Department Desecription")
    banner = models.ImageField("Department Banner", upload_to='images/department/', default='images/department/wallowalake.JPG')

    class Meta:
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