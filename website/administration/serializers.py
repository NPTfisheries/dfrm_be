#administration/serializers.py
from rest_framework import serializers
from common.serializers import BaseModelSerializer
from account.serializers import UserSerializer
from files.serializers import ImageSerializer
from account.models import User
from administration.models import Department, Division, Project, Subproject, Task


class BaseImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)




class BaseAdminSerializer(BaseModelSerializer):

    def to_representation(self, instance):
        # Override the 'user' field representation for GET requests
        if self.context['request'].method == 'GET':
            return {
                **super().to_representation(instance),
                'manager': UserSerializer(instance.manager).data,
                'deputy': UserSerializer(instance.deputy).data,
                'assistant': UserSerializer(instance.assistant).data,
                'staff': UserSerializer(instance.staff.all(), many=True).data,
                'img_banner': ImageSerializer(instance.img_banner).data,
                'img_card': ImageSerializer(instance.img_card).data
            }
        return super().to_representation(instance)

    def create(self, validated_data):
        ids = validated_data.pop('staff')
        instance = super().create(validated_data)
        instance.staff.set(ids)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        ids = validated_data.pop('staff')
        instance = super().update(instance, validated_data)
        instance.staff.set(ids)
        instance.save()
        return instance

class DepartmentSerializer(BaseAdminSerializer):
    class Meta:
        model = Department
        fields = ['id', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card']


class DivisionSerializer(BaseAdminSerializer):
    class Meta:
        model = Division
        fields = ['id', 'department', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card']


class ProjectSerializer(BaseModelSerializer):
    project_leader = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Project
        fields = ['id', 'department', 'slug', 'name', 'description', 'project_leader', 'img_banner', 'img_card']

    def to_representation(self, instance):
        # Override the 'user' field representation for GET requests
        if self.context['request'].method == 'GET':
            return {
                **super().to_representation(instance),
                'project_leader': UserSerializer(instance.project_leader.all(), many=True).data,
                'img_banner': ImageSerializer(instance.img_banner).data,
                'img_card': ImageSerializer(instance.img_card).data
            }
        return super().to_representation(instance)

    def create(self, validated_data):
        ids = validated_data.pop('project_leader')
        instance = super().create(validated_data)
        instance.project_leader.set(ids)
        return instance

    def update(self, instance, validated_data):
        ids = validated_data.pop('project_leader')
        instance = super().update(instance, validated_data)
        instance.project_leader.set(ids)
        instance.save()
        return instance

    
class SubprojectSerializer(BaseModelSerializer):
    class Meta:
        model = Subproject
        fields = ['id', 'project', 'slug', 'name', 'description', 'lead', 'img_banner', 'img_card']

    def to_representation(self, instance):
        # Override the 'user' field representation for GET requests
        if self.context['request'].method == 'GET':
            return {
                **super().to_representation(instance),
                'lead': UserSerializer(instance.lead).data,
                'img_banner': ImageSerializer(instance.img_banner).data,
                'img_card': ImageSerializer(instance.img_card).data
            }
        return super().to_representation(instance)  

class TaskSerializer(BaseModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'subproject', 'slug', 'name', 'description', 'supervisor', 'img_banner', 'img_card']

    def to_representation(self, instance):
        # Override the 'user' field representation for GET requests
        if self.context['request'].method == 'GET':
            return {
                **super().to_representation(instance),
                'supervisor': UserSerializer(instance.supervisor).data,
                'img_banner': ImageSerializer(instance.img_banner).data,
                'img_card': ImageSerializer(instance.img_card).data
            }
        return super().to_representation(instance)   
