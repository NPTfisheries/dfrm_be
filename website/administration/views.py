from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from administration.models import Department, Division, Project, Subproject, Task
from administration.serializers import DepartmentSerializer, DivisionSerializer, ProjectSerializer, SubprojectSerializer, TaskSerializer

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

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]