from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from administration.models import Department, Division, Project, Subproject, Task, Facility
from administration.serializers import DepartmentSerializer, DivisionSerializer, ProjectSerializer, GETSubprojectSerializer, SubprojectSerializer, TaskSerializer, FacilitySerializer
from common.views import CustomObjectPermissions
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

    # @action(detail=True, methods=['get'])
    def projects(self, request, slug=None):
        division = self.get_object()
        subprojects = Subproject.objects.filter(division=division).distinct()
        project_ids = subprojects.values_list('project', flat=True)
        projects = Project.objects.filter(id__in=project_ids)
        print(f'Debug projects: {projects}')
        if projects is not None:
            serializer = ProjectSerializer(projects, many=True, context={'request': request})
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = serializer.data

        projects_data = self.projects(request, slug=kwargs['slug']).data\
        # projects_data = []
        print(f'Debug projects_data: {projects_data}')
        if projects_data is not None:
            response_data['projects'] = projects_data
            
        return Response(response_data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [CustomObjectPermissions]

class SubprojectViewSet(viewsets.ModelViewSet):
    queryset = Subproject.objects.all()    
    # serializer_class = SubprojectSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_serializer_class(self):
        # Check the HTTP request method to determine which serializer to use
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return SubprojectSerializer
        return GETSubprojectSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get('project_id')

        if project_id:
            project= get_object_or_404(Project, id=project_id)
            return Subproject.objects.filter(project=project).order_by('sort_order', 'name')
        else:
            return Subproject.objects.all().order_by('sort_order', 'name')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #lookup_field = 'slug'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        subproject_id = self.request.query_params.get('subproject_id')

        if subproject_id:
            subproject= get_object_or_404(Subproject, id=subproject_id)
            return Task.objects.filter(subproject=subproject).order_by('sort_order', 'task_type')
        else:
            return Task.objects.all().order_by('sort_order', 'task_type')

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