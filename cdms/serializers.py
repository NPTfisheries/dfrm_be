from common.serializers import MetaModelSerializer
from cdms.models import Location, Dataset, Instrument, Activity, Field

class LocationSerializer(MetaModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'description', 'latitude', 'longitude', 'elevation', 'river_kilometer', 'projection', 'is_active']

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
        fields = ['id', 'user', 'location', 'project', 'dataset', 'instrument', 'date', 'data']

class FieldSerializer(MetaModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'name', 'description','is_active']