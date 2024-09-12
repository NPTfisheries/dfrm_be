from django.db import models
from django.contrib.postgres.fields import JSONField
from common.models import MetaModel
from account.models import User
from administration.models import Project

# null = True: django will store empty values as NULL in the db.  default False
# blank = True: field is allowed to be blank. default False

class Location(MetaModel):
    class Meta:
        abstract = True
        ordering = ['name']
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.IntegerField(null=True, blank=True)
    river_kilometer = models.FloatField(null=True, blank=True)  # DECIMAL FIELD??
    projection = models.CharField(max_length=100, null=True, blank=True) # BaseSpatialField???
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

    instrument_types = (
        ('Temperature Logger', 'Temperature Logger'),
        ('Multiparameter Probe', 'Multiparameter Probe'),
        ('Field Thermometer', 'Field Thermometer'),
        ('Automated Water Sampler', 'Automated Water Sampler')
        ('Data Tablet', 'Data Tablet')
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_project")
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(choices=instrument_types)
    model = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)

class Activity(MetaModel):   # this will have "is_active"
    class Meta:
        abstract = True
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_location")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_project")
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_dataset")
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_instrument")
    date = models.DateField()
    data = JSONField()  # null=True, blank=True ?? allow for a no-data header?

# all the options for ColDefs for AG Grid.  I added dataset and required
class Field(models.Model):
    class Meta:
        abstract = True
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_dataset")
    required = models.BooleanField(default=False)
    header_name = models.CharField(max_length=255, help_text="The display name for the column header")
    field = models.CharField(max_length=255, help_text="The data field for the column")
    sortable = models.BooleanField(default=True, help_text="Whether the column is sortable")
    filterable = models.BooleanField(default=True, help_text="Whether the column can be filtered")
    resizable = models.BooleanField(default=True, help_text="Whether the column can be resized")
    editable = models.BooleanField(default=False, help_text="Whether the column is editable")
    checkbox_selection = models.BooleanField(default=False, help_text="Whether to display a checkbox selection")
    pinned = models.CharField(max_length=10, choices=[('left', 'Left'), ('right', 'Right'), ('none', 'None')], default='none', help_text="Whether the column is pinned to the left or right")
    width = models.IntegerField(null=True, blank=True, help_text="The width of the column in pixels", null=True, blank=True)
    min_width = models.IntegerField(null=True, blank=True, help_text="The minimum width of the column in pixels", null=True, blank=True)
    max_width = models.IntegerField(null=True, blank=True, help_text="The maximum width of the column in pixels", null=True, blank=True)
    hide = models.BooleanField(default=False, help_text="Whether the column is hidden by default")
    cell_renderer = models.CharField(max_length=255, null=True, blank=True, help_text="Custom cell renderer for the column", null=True, blank=True)
    cell_style = models.TextField(null=True, blank=True, help_text="CSS styles to be applied to the cell", null=True, blank=True)
    cell_class = models.TextField(null=True, blank=True, help_text="CSS classes to be applied to the cell", null=True, blank=True)
    value_formatter = models.CharField(max_length=255, null=True, blank=True, help_text="Custom value formatter function for the column", null=True, blank=True)
    header_tooltip = models.CharField(max_length=255, null=True, blank=True, help_text="Tooltip to be shown when the user hovers over the header", null=True, blank=True)

    def __str__(self):
        return self.header_name
    