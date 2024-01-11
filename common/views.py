from .models import ObjectLookUp
from .serializers import ObjectLookUpSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import permissions

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
        

# Object-Level Permissions
class CustomObjectPermissions(permissions.DjangoObjectPermissions):

    def get_permission_names(self, view):
        # Get the model class associated with the ViewSet
        model = view.queryset.model if hasattr(view, 'queryset') else view.model
        app_label = model._meta.app_label
        model_name = model.__name__.lower()
        
        # Define permission names based on the app_label and model_name
        change_permission_name = f"{app_label}.change_{model_name}"
        delete_permission_name = f"{app_label}.delete_{model_name}"
        
        return {
            'change_permission_name': change_permission_name,
            'delete_permission_name': delete_permission_name
        }

    def has_permission(self, request, view):
        # Allow anyone to view
        if request.method in permissions.SAFE_METHODS:
            return True

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        permission_names = self.get_permission_names(view)
        # Check for change and delete permissions

        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm(permission_names['change_permission_name'], obj)
        
        if request.method == 'DELETE':           
            return request.user.has_perm(permission_names['delete_permission_name'], obj)
            
        return super().has_object_permission(request, view, obj)