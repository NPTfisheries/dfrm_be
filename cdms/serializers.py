from common.serializers import MetaModelSerializer
from rest_framework import serializers
from cdms.models import Dataset, Instrument, Field, Activity
from administration.models import Project
from administration.serializers import ProjectSerializer

# class LocationSerializer(MetaModelSerializer):
#     class Meta:
#         model = Location
#         fields = ['id', 'name', 'description', 'latitude', 'longitude', 'elevation', 'river_kilometer', 'projection', 'is_active']

class DatasetSerializer(MetaModelSerializer):
    class Meta:
        model = Dataset
        fields = ['id', 'name', 'description','is_active']

class InstrumentSerializer(MetaModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name', 'description', 'project', 'type', 'model', 'serial_number', 'manufacturer', 'is_active']

class ActivitySerializer(MetaModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'project', 'dataset', 'date', 'data'] # location, instrument
        depth = 0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Check if 'request' exists in context and is a GET request
        request = self.context.get('request', None)
        if request and request.method == 'GET':
            self.Meta.depth = 2  # Set depth to 2 for GET requests
        else:
            self.Meta.depth = 0  # Set depth to 1 for all others


class FieldSerializer(MetaModelSerializer):
    class Meta:
        model = Field
        fields = [
            'id', 'sortingOrder','dataset', 'required', 'headerName', 'field', 'sortable', 'filter', 'resizable', 'editable', 
            'pinned', 'width', 'minWidth', 'maxWidth', 'hide', 'cellRenderer', 'cellStyle', 'cellClass', 
            'valueFormatter', 'headerTooltip', 'cellEditor', 'cellEditorParams' ]