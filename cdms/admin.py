from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from cdms.models import Activity, Instrument, Field

# # Register your models here.
# @admin.register(Location)
# class LocationClassAdmin(admin.OSMGeoAdmin):
#     list_display = ('id', 'name', 'description', 'latitude', 'longitude', 'elevation', 'river_kilometer', 'projection')

@admin.register(Instrument)
class InstrumentClassAdmin(GuardedModelAdmin):
    list_display = ('id', 'project', 'name', 'description', 'type', 'model', 'serial_number', 'manufacturer')

@admin.register(Activity)
class ActivityClassAdmin(GuardedModelAdmin):
    list_display = ('id', 'activity_id', 'task', 'date', 'header', 'detail') # location, instrument

@admin.register(Field)
class FieldClassAdmin(GuardedModelAdmin):
    list_display = ('id', 'sortingOrder', 'task_type', 'required', 'headerName', 'field', 'filter', 'editable', 
                    'pinned', 'width', 'minWidth', 'maxWidth', 'hide', 'cellRenderer', 'cellStyle', 'cellClass', 
                    'valueFormatter', 'headerTooltip', 'cellEditor', 'cellEditorParams')