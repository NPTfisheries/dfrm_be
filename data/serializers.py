# from common.serializers import MetaModelSerializer
# from rest_framework import serializers
# from data.models import Instrument, Field, Activity

# class InstrumentSerializer(MetaModelSerializer):
#     class Meta:
#         model = Instrument
#         fields = ['id', 'name', 'description', 'instrument_type', 'model', 'serial_number', 'manufacturer', 'display_name', 'is_active']

# class ActivitySerializer(MetaModelSerializer):
#     class Meta:
#         model = Activity
#         fields = ['id', 'activity_id', 'location', 'instrument', 'task', 'header', 'detail', 'updated_at']
#         depth = 0
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Check if 'request' exists in context and is a GET request
#         request = self.context.get('request', None)
#         if request and request.method == 'GET':
#             self.Meta.depth = 2  # Set depth to 2 for GET requests
#         else:
#             self.Meta.depth = 0  # Set depth to 1 for all others


# class FieldSerializer(MetaModelSerializer):
#     class Meta:
#         model = Field
#         fields = [
#             'id', 'task_type', 'field_for', 'sortingOrder', 'required', 'headerName', 'field', 'filter', 'editable', 
#             'pinned', 'width', 'minWidth', 'maxWidth', 'hide', 'cellRenderer', 'cellStyle', 'cellClass', 
#             'valueFormatter', 'headerTooltip', 'cellEditor', 'cellEditorParams']