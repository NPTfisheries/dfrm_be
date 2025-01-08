from rest_framework import viewsets, permissions
from data.models import Activity, Instrument, Field
from common.models import ObjectLookUp
from data.serializers import ActivitySerializer, InstrumentSerializer, FieldSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

# class InstrumentViewSet(viewsets.ModelViewSet):
#     queryset = Instrument.objects.all()
#     serializer_class = InstrumentSerializer
#     lookup_field = 'name'
#     permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'activity_id'   # important!
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

# class FieldViewSet(viewsets.ModelViewSet):
#     queryset = Field.objects.all()
#     serializer_class = FieldSerializer
#     lookup_field = 'id'
#     permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        task_type = self.request.query_params.get('task_type')

        # always include activity fields
        activity_field_task_types = ObjectLookUp.objects.filter(name="Activity Field").values_list('id', flat=True)

        if task_type:
            combined_task_types = list(activity_field_task_types) + [task_type]
            return Field.objects.filter(task_type__id__in=combined_task_types)
        
        return Field.objects.all()