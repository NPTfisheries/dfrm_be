from common.serializers import MetaModelSerializer
from location.models import Location

class LocationSerializer(MetaModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'