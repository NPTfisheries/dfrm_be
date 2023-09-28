from django.shortcuts import render
from .models import ObjectLookUp
from .serializers import ObjectLookUpSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.
class ObjectLookUpView(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectLookUp.objects.all()
    serializer_class = ObjectLookUpSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        object_type = self.request.query_params.get('object_type')

        if not object_type:
            return ObjectLookUp.objects.all()
        else:
            return ObjectLookUp.objects.filter(object_type=object_type)