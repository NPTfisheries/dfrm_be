from rest_framework import viewsets
from files.models import Image, Document
from files.serializers import ImageSerializer, DocumentSerializer
from common.views import CustomObjectPermissions


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [CustomObjectPermissions]

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [CustomObjectPermissions]