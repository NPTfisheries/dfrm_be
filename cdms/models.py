from django.db import models
from django.utils import timezone
from common.models import MetaModel
from location.models import Location
from administration.models import Project, Task
from account.models import User
from common.models import ObjectLookUp
from django.contrib.postgres.fields import ArrayField

# null = True: django will store empty values as NULL in the db.  default False
# blank = True: field is allowed to be blank. default False

class Instrument(MetaModel):
    # Task????
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    instrument_type = models.ForeignKey(ObjectLookUp, on_delete=models.PROTECT, limit_choices_to={'object_type': 'Instrument'}, related_name="%(class)s_object_lookups")
    model = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)

    @property
    def display_name(self):
        return f"{self.name} ({self.serial_number})"
    

    def __str__(self):
        return self.name + " (" + self.serial_number + ")" 

class Activity(models.Model):
    # set once, never change.
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_created_by")
    activity_id = models.IntegerField(editable=False, unique=True)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    # updated each edit
    effective_date = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_edited_by")
    
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, null=True, blank=True)
    header = models.JSONField(default=list)  # header should include Survey Date, Calculation Date, etc.  (NO ACTIVITY DATE)
    detail = models.JSONField(default=list)  # null=True, blank=True ?? allow for a no-data header?

    def save(self, *args, **kwargs):
        if not self.activity_id:
            max_id = Activity.objects.aggregate(models.Max('activity_id'))['activity_id_max']
            self.activity_id = (max_id or 0) +1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

# https://www.ag-grid.com/javascript-data-grid/column-properties/  
class Field(models.Model):
    task_type = models.ForeignKey(ObjectLookUp, on_delete=models.PROTECT, limit_choices_to={'object_type': 'Task'})
    field_for = models.CharField(choices=(('header','Header'),('detail','Detail')))
    required = models.BooleanField(default=False)

    field = models.CharField(max_length=255, help_text="The data field for the column")
    headerName = models.CharField(max_length=255, help_text="The display name for the column header")
    headerTooltip = models.CharField(max_length=255, null=True, blank=True, help_text="Tooltip to be shown when the user hovers over the header")
    sortingOrder = models.IntegerField(default=1, null=True, blank=True, help_text="Establishes column order in AG Grid")
    editable = models.BooleanField(default=False, help_text="Whether the column is editable")
    filter = models.BooleanField(default=True, help_text="Whether the column can be filtered - Grid will determine filter based on datatype.")
    pinned = models.CharField(null=True, blank=True, max_length=10, choices=[('left', 'Left'), ('right', 'Right')], help_text="Whether the column is pinned to the left or right")
    width = models.IntegerField(null=True, blank=True, help_text="The width of the column in pixels")
    minWidth = models.IntegerField(null=True, blank=True, help_text="The minimum width of the column in pixels")
    maxWidth = models.IntegerField(null=True, blank=True, help_text="The maximum width of the column in pixels")
    hide = models.BooleanField(default=False, help_text="Whether the column is hidden by default")  
    cellRenderer = models.CharField(max_length=255, null=True, blank=True, help_text="Custom cell renderer for the column")
    cellStyle = models.JSONField(null=True, blank=True, help_text="An object of CSS styles to be applied to the cell. ")
    cellClass = ArrayField(models.CharField(max_length=100), null=True, blank=True, help_text="CSS classes to be applied to the cell. Array of strings (classes).")
    valueFormatter = models.CharField(max_length=255, null=True, blank=True, help_text="Custom value formatter function for the column")
    cellEditor = models.TextField(null=True, blank=True)
    cellEditorParams = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.headerName
    
    class Meta:
        ordering = ['sortingOrder']
        
# class Protocol(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     date_started = models.DateField()
#     date_ended = models.DateField(blank=True, null=True)
#     url = models.URLField(max_length=255, blank=True, null=True)

# class Contract(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     date_started = models.DateField()
#     date_ended = models.DateField(blank=True, null=True)