import os 
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from files.models import Image, Document
from files.serializers import ImageSerializer, DocumentSerializer
from common.views import CustomObjectPermissions
from rest_framework.permissions import IsAuthenticated

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [CustomObjectPermissions]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print('DESTROY IMAGE!', flush=True)

        # Get the file path from the instance
        file_path = instance.image.path
        print('Image Key:', file_path, flush=True)

        # Delete the file from local storage (dev)
        if os.path.exists(file_path):
            os.remove(file_path)

        # Delete the database record
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [CustomObjectPermissions]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Get the file path from the instance
        file_path = instance.document.path

        # Delete the file from the storage
        if os.path.exists(file_path):
            os.remove(file_path)

        # Delete the database record
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)