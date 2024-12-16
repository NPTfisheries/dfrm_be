from rest_framework import viewsets, permissions
from .models import InvasiveSpecies
from .serializers import InvasiveSpeciesSerializer

# Create your views here.

class InvasiveSpeciesViewSet(viewsets.ModelViewSet):
    queryset = InvasiveSpecies.objects.all()
    serializer_class = InvasiveSpeciesSerializer
    lookup_field = 'name'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]