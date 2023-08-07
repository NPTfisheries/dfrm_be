from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from administration.models import Department, Division, Project
from administration.serializers import DepartmentSerializer, DivisionSerializer, ProjectSerializer
# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = [IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]