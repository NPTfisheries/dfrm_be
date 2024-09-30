from rest_framework import viewsets
from rest_framework import permissions
from cdms.models import Activity, Instrument, Field
from cdms.serializers import ActivitySerializer, InstrumentSerializer, FieldSerializer
from django.shortcuts import get_object_or_404

# class LocationViewSet(viewsets.ModelViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#     lookup_field = 'name'
#     permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

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
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    lookup_field = 'id'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    # def get_queryset(self):
    #     dataset_id = self.request.query_params.get('dataset_id')

    #     if dataset_id:
    #         dataset= get_object_or_404(O, id=dataset_id)
    #         return Field.objects.filter(dataset=dataset)
    #     else:
    #         return Field.objects.all()