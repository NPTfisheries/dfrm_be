from rest_framework import viewsets
from rest_framework import permissions
from cdms.models import Location, Dataset, Instrument, Activity, Field
from cdms.serializers import LocationSerializer, DatasetSerializer, InstrumentSerializer, ActivitySerializer, FieldSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'name'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    lookup_field = 'name'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    lookup_field = 'name'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'id'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class FieldViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = FieldSerializer
    lookup_field = 'id'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]