from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from administration.models import Department, Division, Project, Task, Facility
from administration.serializers import DepartmentSerializer, DivisionSerializer, ProjectSerializer, TaskSerializer, TaskDetailSerializer, FacilitySerializer
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
        tasks = Task.objects.filter(division=division).distinct()
        project_ids = tasks.values_list('project', flat=True)
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

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]  # is this wrong??
    # permission_classes = [CustomObjectPermissions]  # is this correct??

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskDetailSerializer
        return TaskSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get('project_id')

        if project_id:
            project= get_object_or_404(Project, id=project_id)
            return Task.objects.filter(project=project).order_by('sort_order', 'task_type')
        else:
            return Task.objects.all().order_by('sort_order', 'task_type')

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    lookup_field = 'slug'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Access the data returned by the serializer
        serialized_data = serializer.data

        # Return the features array directly
        return Response(serialized_data['features'])
    
    def create(self, request, *args, **kwargs):
        # Print the request data
        print(request.data)

        # Continue with the regular create method
        return super().create(request, *args, **kwargs)