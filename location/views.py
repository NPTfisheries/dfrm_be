from rest_framework import viewsets, permissions
from rest_framework.response import Response
from location.models import Location
from location.serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'id'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Access the data returned by the serializer
        serialized_data = serializer.data

        # Return the features array directly
        return Response(serialized_data['features'])

