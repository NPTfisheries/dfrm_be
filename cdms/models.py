from django.db import models
from django.contrib.postgres.fields import JSONField
from common.models import MetaModel
from account.models import User
from administration.models import Project

class Location(MetaModel):
    class Meta:
        abstract = True
        ordering = ['name']
    name = models.CharField(max_length=300)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.IntegerField()
    river_kilometer = models.FloatField()
    projection = models.CharField(max_length=100)
    # sde_feature_class_id
    # timezone

class Dataset(MetaModel):
    class Meta:
        abstract = True
        ordering = ['name']
    name = models.CharField(max_length=300)
    description = models.TextField()

class Instrument(MetaModel):
    class Meta:
        abstract = True
        ordering = ['name']
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=300)
    description = models.TextField()
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)

class Activity(MetaModel):   # this will have "is_active"
    class Meta:
        abstract = True
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    project = models.ForeignKey(Project)
    dataset = models.ForeignKey(Dataset)
    instrument = models.ForeignKey(Instrument)
    date = models.DateField()
    data = JSONField()

# we need to include everything needed for ag grid, and replicate here.
class Field(models.Model):
    class Meta:
        abstract = True
    dataset = models.ForeignKey(Dataset)
    header_name = models.CharField(max_length=255, help_text="The display name for the column header")
    field = models.CharField(max_length=255, help_text="The data field for the column")
    sortable = models.BooleanField(default=True, help_text="Whether the column is sortable")
    filterable = models.BooleanField(default=True, help_text="Whether the column can be filtered")
    resizable = models.BooleanField(default=True, help_text="Whether the column can be resized")
    editable = models.BooleanField(default=False, help_text="Whether the column is editable")
    checkbox_selection = models.BooleanField(default=False, help_text="Whether to display a checkbox selection")
    pinned = models.CharField(max_length=10, choices=[('left', 'Left'), ('right', 'Right'), ('none', 'None')], default='none', help_text="Whether the column is pinned to the left or right")
    width = models.IntegerField(null=True, blank=True, help_text="The width of the column in pixels")
    min_width = models.IntegerField(null=True, blank=True, help_text="The minimum width of the column in pixels")
    max_width = models.IntegerField(null=True, blank=True, help_text="The maximum width of the column in pixels")
    hide = models.BooleanField(default=False, help_text="Whether the column is hidden by default")
    cell_renderer = models.CharField(max_length=255, null=True, blank=True, help_text="Custom cell renderer for the column")
    cell_style = models.TextField(null=True, blank=True, help_text="CSS styles to be applied to the cell")
    cell_class = models.TextField(null=True, blank=True, help_text="CSS classes to be applied to the cell")
    value_formatter = models.CharField(max_length=255, null=True, blank=True, help_text="Custom value formatter function for the column")
    header_tooltip = models.CharField(max_length=255, null=True, blank=True, help_text="Tooltip to be shown when the user hovers over the header")

    def __str__(self):
        return self.header_name
    