# from django.contrib import admin
# from guardian.admin import GuardedModelAdmin
# from data.models import Activity, Instrument, Field

# @admin.register(Instrument)
# class InstrumentClassAdmin(GuardedModelAdmin):
#     list_display = ('id', 'name', 'description', 'instrument_type', 'model', 'serial_number', 'manufacturer')

# @admin.register(Activity)
# class ActivityClassAdmin(GuardedModelAdmin):
#     list_display = ('id', 'activity_id', 'location', 'instrument', 'task', 'header', 'detail') 

# @admin.register(Field)
# class FieldClassAdmin(GuardedModelAdmin):
#     list_display = ('id', 'sortingOrder', 'task_type', 'required', 'headerName', 'field', 'filter', 'editable', 
#                     'pinned', 'width', 'minWidth', 'maxWidth', 'hide', 'cellRenderer', 'cellStyle', 'cellClass', 
#                     'valueFormatter', 'headerTooltip', 'cellEditor', 'cellEditorParams')