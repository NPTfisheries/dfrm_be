from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from files.models import Image
from files.serializers import ImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # lookup_field = 'slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
