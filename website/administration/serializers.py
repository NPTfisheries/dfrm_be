#admin/serializers.py
from rest_framework import serializers
from account.serializers import UserSerializer
from account.models import User
from administration.models import Department, Division, Project, Subproject, Task


class AdminModelSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        extra_kwargs = {
            'created_by': {'read_only': True},
            'updated_by': {'read_only': True},
            'slug': {'read_only': True},
            'url': {'lookup_field': 'slug'}
        }

    def create(self, validated_data):
        # get authenticated user
        user = self.context['request'].user
        # create a new instance
        instance = self.Meta.model.objects.create(
            created_by=user,
            updated_by=user,
            is_active=True,
            **validated_data
        )
        return instance

    def update(self, instance, validated_data):
        # get authenticated user
        user = self.context['request'].user
        # Update model instance with the values supplied in the request.
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.updated_by = user
        instance.save()
        return instance


class DepartmentSerializer(AdminModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff']
        
    def create(self, validated_data):
        ids = validated_data.pop('staff')
        instance = super().create(validated_data)
        instance.staff.set(ids)
        return instance   

class DivisionSerializer(AdminModelSerializer):
    #department = DepartmentSerializer() # creates a nested JSON object where department is an object with all department fields.
    # leaving the above line commented out will only allow POST body to only have pk, and get requests will only have department pk
    class Meta:
        model = Division
        fields = ['id', 'department', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff']

    def create(self, validated_data):
        ids = validated_data.pop('staff')
        instance = super().create(validated_data)
        instance.staff.set(ids)
        return instance  

class ProjectSerializer(AdminModelSerializer):
    project_leader = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Project
        fields = ['id', 'slug', 'name', 'description', 'project_leader']

    def create(self, validated_data):
        ids = validated_data.pop('project_leader')
        instance = super().create(validated_data)
        instance.project_leader.set(ids)
        return instance
    
class SubprojectSerializer(AdminModelSerializer):
    class Meta:
        model = Subproject
        fields = ['id', 'project', 'slug', 'name', 'description', 'lead']  

class TaskSerializer(AdminModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'subproject', 'slug', 'name', 'description', 'supervisor'] 
