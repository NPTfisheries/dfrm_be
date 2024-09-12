from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from cdms.models import Dataset, Instrument, Field

# # Register your models here.
# @admin.register(Location)
# class LocationClassAdmin(admin.OSMGeoAdmin):
#     list_display = ('id', 'name', 'description', 'latitude', 'longitude', 'elevation', 'river_kilometer', 'projection')

@admin.register(Dataset)
class DatasetClassAdmin(GuardedModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Instrument)
class InstrumentClassAdmin(GuardedModelAdmin):
    list_display = ('id', 'project', 'name', 'description', 'type', 'model', 'serial_number', 'manufacturer')

# @admin.register(Activity)
# class ActivityClassAdmin(GuardedModelAdmin):
#     list_display = ('id', 'user', 'location', 'project', 'dataset', 'instrument', 'date', 'data')

@admin.register(Field)
class FieldClassAdmin(GuardedModelAdmin):
    list_display = ('id', 'dataset', 'header_name', 'field', 'sortable', 'filterable', 'resizable', 'editable', 'checkbox_selection', 
            'pinned', 'width', 'min_width', 'max_width', 'hide', 'cell_renderer', 'cell_style', 'cell_class', 
            'value_formatter', 'header_tooltip')