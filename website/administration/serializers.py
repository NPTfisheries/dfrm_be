#administration/serializers.py
from rest_framework import serializers
from common.serializers import BaseModelSerializer
from account.models import User
from administration.models import Department, Division, Project, Subproject, Task

class DepartmentSerializer(BaseModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card']
        
    def create(self, validated_data):
        ids = validated_data.pop('staff')
        instance = super().create(validated_data)
        instance.staff.set(ids)
        return instance   

class DivisionSerializer(BaseModelSerializer):
    #department = DepartmentSerializer() # creates a nested JSON object where department is an object with all department fields.
    # leaving the above line commented out will only allow POST body to only have pk, and get requests will only have department pk
    class Meta:
        model = Division
        fields = ['id', 'department', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card']

    def create(self, validated_data):
        ids = validated_data.pop('staff')
        instance = super().create(validated_data)
        instance.staff.set(ids)
        return instance  

class ProjectSerializer(BaseModelSerializer):
    project_leader = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Project
        fields = ['id', 'slug', 'name', 'description', 'project_leader', 'img_banner', 'img_card']

    def create(self, validated_data):
        ids = validated_data.pop('project_leader')
        instance = super().create(validated_data)
        instance.project_leader.set(ids)
        return instance
    
class SubprojectSerializer(BaseModelSerializer):
    class Meta:
        model = Subproject
        fields = ['id', 'project', 'slug', 'name', 'description', 'lead', 'img_banner', 'img_card']  

class TaskSerializer(BaseModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'subproject', 'slug', 'name', 'description', 'supervisor', 'img_banner', 'img_card'] 
