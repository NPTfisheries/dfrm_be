from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from administration.models import Department, Division, Project, Subproject, Task
from administration.serializers import DepartmentSerializer, DivisionSerializer, ProjectSerializer, SubprojectSerializer, TaskSerializer

from django.shortcuts import get_object_or_404

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    lookup_field = 'slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class SubprojectViewSet(viewsets.ModelViewSet):
    queryset = Subproject.objects.all()    
    serializer_class = SubprojectSerializer
    lookup_field = 'slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

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
    lookup_field = 'slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        subproject_id = self.request.query_params.get('subproject_id')

        if subproject_id:
            subproject= get_object_or_404(Subproject, id=subproject_id)
            return Task.objects.filter(subproject=subproject)
        else:
            return Task.objects.all();