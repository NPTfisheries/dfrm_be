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
    dataset = serializers.PrimaryKeyRelatedField(queryset=Dataset.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Activity
        fields = ['id', 'project', 'dataset', 'date', 'data'] # location, instrument

    def to_representation(self, instance):
        # Override field representation for GET requests
        ret = super().to_representation(instance)
        if self.context['request'].method == 'GET':
            ret['dataset'] = DatasetSerializer(instance.dataset).data
            ret['project'] = ProjectSerializer(instance.project).data
        return ret

class FieldSerializer(MetaModelSerializer):
    class Meta:
        model = Field
        fields = [
            'id', 'sortingOrder','dataset', 'required', 'headerName', 'field', 'sortable', 'filter', 'resizable', 'editable', 
            'pinned', 'width', 'minWidth', 'maxWidth', 'hide', 'cellRenderer', 'cellStyle', 'cellClass', 
            'valueFormatter', 'headerTooltip', 'cellEditor', 'cellEditorParams' ]