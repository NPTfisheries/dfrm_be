from common.serializers import MetaModelSerializer
from rest_framework import serializers
from data.models import Instrument, Field, Activity

class InstrumentSerializer(MetaModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name', 'description', 'instrument_type', 'model', 'serial_number', 'manufacturer', 'display_name', 'is_active']

class ActivitySerializer(MetaModelSerializer):
    task_type_name = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'activity_id', 'location', 'instrument', 'task', 'task_type_name', 'header', 'detail', 'updated_at']
        depth = 0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Check if 'request' exists in context and is a GET request
        request = self.context.get('request', None)
        if request and request.method == 'GET':
            self.Meta.depth = 1  # Set depth to 1 for GET requests
        else:
            self.Meta.depth = 0  # Set depth to 1 for all others
    
    def get_task_type_name(self, obj):
        if obj.task and obj.task.task_type:
            return obj.task.task_type.name
        return None


class FieldSerializer(MetaModelSerializer):
    class Meta:
        model = Field
        fields = [
            'id', 'task_type', 'field_for', 'sortingOrder', 'required', 'headerName', 'field', 'filter', 'editable', 
            'pinned', 'width', 'minWidth', 'maxWidth', 'hide', 'cellRenderer', 'cellStyle', 'cellClass', 
            'valueFormatter', 'headerTooltip', 'cellEditor', 'cellEditorParams']