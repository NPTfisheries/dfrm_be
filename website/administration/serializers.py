#admin/serializers.py
from rest_framework import serializers
from account.serializers import UserSerializer
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
        fields = ['id', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'img_banner', 'img_card']
        #fields = '__all__'   

class DivisionSerializer(AdminModelSerializer):
    #department = DepartmentSerializer() # creates a nested JSON object where department is an object with all department fields.
    # leaving the above line commented out will only allow POST body to only have pk, and get requests will only have department pk
    class Meta:
        model = Division
        fields = ['id', 'department', 'name', 'description', 'manager', 'deputy', 'assistant', 'img_banner', 'img_card']

class ProjectSerializer(AdminModelSerializer):
    project_leader = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'project_leader', 'img_banner', 'img_card']    

class SubprojectSerializer(AdminModelSerializer):
    class Meta:
        model = Subproject
        fields = '__all__'    

class TaskSerializer(AdminModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
