from common.serializers import MetaModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from location.models import Location

class LocationSerializer(MetaModelSerializer, GeoFeatureModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'description', 'geometry']
        geo_field = 'geometry'
