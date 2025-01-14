# common/models.py
from django.db import models
from django.template.defaultfilters import slugify
from account.models import User

# Abstract model classes for reuse across multiple apps.
class MetaModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_creator")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_editor")
    is_active = models.BooleanField(default=True)
    display = models.BooleanField(default=True)

    class Meta:
        abstract = True

class BaseModel(MetaModel):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    slug = models.SlugField(null=True, unique=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.pk: # if self.pk is blank
            self.slug = slugify(self.name)
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name

class ObjectLookUp(MetaModel):
    # Adding a new object type to this list shouldn't require a new migration.
    OBJECT_TYPE = (
        ('Document', 'Document'),
        ('Facility', 'Facility'),
        ('Instrument', 'Instrument'),
        ('Invasive', 'Invasive'),
        ('Task', 'Task')
    )

    object_type = models.CharField(choices = OBJECT_TYPE)
    name = models.CharField(max_length=300)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['object_type', 'name'], name='unique_object_type_name')
        ]
        ordering = ['name']

    def __str__(self):
        return self.name;
