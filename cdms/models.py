from django.db import models
from common.models import MetaModel
from account.models import User
from administration.models import Project

# null = True: django will store empty values as NULL in the db.  default False
# blank = True: field is allowed to be blank. default False

class Location(MetaModel):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.IntegerField(null=True, blank=True)
    river_kilometer = models.FloatField(null=True, blank=True)  # DECIMAL FIELD??
    projection = models.CharField(max_length=100, null=True, blank=True)
    trt_pop_id = models.CharField(max_length=20, null=True, blank=True)
    # sde_feature_class_id
    # timezone

# class Population(): TRT_POPID??

class Dataset(MetaModel):
    name = models.CharField(max_length=300)
    description = models.TextField()
    # summary_dataset = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Instrument(MetaModel):
    INSTRUMENT_TYPE = (
        ('Temperature Logger','Temperature Logger'),
        ('Multiparameter Probe','Multiparameter Probe'),
        ('Field Thermometer','Field Thermometer'),
        ('Automated Water Sampler', 'Automated Water Sampler'),
        ('Data Tablet', 'Data Tablet')
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(choices = INSTRUMENT_TYPE)
    model = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return self.name  # include serial?

class Activity(MetaModel):   # this will have "is_active"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    date = models.DateField()
    data = models.JSONField()  # null=True, blank=True ?? allow for a no-data header?

# all the options for ColDefs for AG Grid.  I added dataset and required
class Field(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_supervisor")
    required = models.BooleanField(default=False)
    headerName = models.CharField(max_length=255, help_text="The display name for the column header")
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
    # type ? https://www.ag-grid.com/angular-data-grid/column-definitions/
    # sort_order?
    # accepted_values?

    def __str__(self):
        return self.header_name
    