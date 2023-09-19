from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from guardian.shortcuts import assign_perm
from administration.models import Department, Division, Project, Subproject, Task, Facility
from administration.serializers import DepartmentSerializer, DivisionSerializer, ProjectSerializer, SubprojectSerializer, TaskSerializer, FacilitySerializer
from django.shortcuts import get_object_or_404

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


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

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [CustomObjectPermissions]

class SubprojectViewSet(viewsets.ModelViewSet):
    queryset = Subproject.objects.all()    
    serializer_class = SubprojectSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        project_id = self.request.query_params.get('project_id')

        if project_id:
            project= get_object_or_404(Project, id=project_id)
            return Subproject.objects.filter(project=project)
        else:
            return Subproject.objects.all();

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #lookup_field = 'slug'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        subproject_id = self.request.query_params.get('subproject_id')

        if subproject_id:
            subproject= get_object_or_404(Subproject, id=subproject_id)
            return Task.objects.filter(subproject=subproject)
        else:
            return Task.objects.all();

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    lookup_field = 'slug'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def create(self, request, *args, **kwargs):
        # Print the request data
        print(request.data)

        # Continue with the regular create method
        return super().create(request, *args, **kwargs)