from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from guardian.shortcuts import assign_perm
from common.serializers import MetaModelSerializer, BaseModelSerializer, ObjectLookUpSerializer
from account.serializers import UserSerializer
from files.serializers import ImageSerializer
from account.models import User
from django.contrib.auth.models import Permission
from administration.models import Department, Division, Project, Task, Facility


class BaseImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)

class BaseAdminSerializer(BaseModelSerializer):

    def to_representation(self, instance):
        # Override field representation for GET requests
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
        fields = ['id', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card', 'is_active']


class DivisionSerializer(BaseAdminSerializer):
    class Meta:
        model = Division
        fields = ['id', 'department', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card', 'is_active']


class ProjectSerializer(BaseModelSerializer):
    project_leader = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Project
        fields = ['id', 'department', 'slug', 'name', 'description', 'project_leader', 'img_banner', 'img_card', 'is_active']

    def to_representation(self, instance):
        # Override field representation for GET requests
        if self.context['request'].method == 'GET':
            return {
                **super().to_representation(instance),
                'project_leader': UserSerializer(instance.project_leader.all(), many=True).data,
                'img_banner': ImageSerializer(instance.img_banner).data,
                'img_card': ImageSerializer(instance.img_card).data
            }
        return super().to_representation(instance)

    def create(self, validated_data):
        user = self.context['request'].user
        ids = validated_data.pop('project_leader')
        instance = super().create(validated_data)
        perm = Permission.objects.get(codename='change_project')
        assign_perm(perm, user, instance)
        print(f'Permission: {perm}')
        for id in ids:
            print(f'DEBUG: Id: {id}')
            assign_perm(perm, id, instance)
        instance.project_leader.set(ids)
        return instance

    def update(self, instance, validated_data):
        ids = validated_data.pop('project_leader')
        instance = super().update(instance, validated_data)
        instance.project_leader.set(ids)
        instance.save()
        return instance

class TaskSerializer(MetaModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'task_type', 'division', 'project', 'supervisor', 'img_banner', 'img_card', 'sort_order', 'is_active']

    def get_task_type(self, instance):
        return ObjectLookUpSerializer(instance.task_type).data;

    def to_representation(self, instance):
        # Override field representation for GET requests
        if self.context['request'].method == 'GET':
            return {
                **super().to_representation(instance),
                'division': DivisionSerializer(instance.division).data,
                'project': ProjectSerializer(instance.project).data,
                'supervisor': UserSerializer(instance.supervisor).data,
                'img_banner': ImageSerializer(instance.img_banner).data,
                'img_card': ImageSerializer(instance.img_card).data,
                'task_type': self.get_task_type(instance),
            }
        return super().to_representation(instance)

    def create(self, validated_data):
        user = self.context['request'].user
        instance = super().create(validated_data)
        perm = Permission.objects.get(codename='change_task')
        assign_perm(perm, user, instance)
        assign_perm(perm, instance.supervisor, instance)
        return instance   

class FacilitySerializer(BaseModelSerializer, GeoFeatureModelSerializer):
   
    class Meta:
        model = Facility
        fields = ['id', 'slug', 'facility_type', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card', 'facility_type', 'phone_number', 'street_address', 'mailing_address', 'city', 'state', 'zipcode', 'is_active']
        geo_field = 'coordinates'

    def get_facility_type(self, instance):
        return ObjectLookUpSerializer(instance.facility_type).data;

    def to_representation(self, instance):
        if self.context['request'].method == 'GET':   
            representation = super().to_representation(instance)
            representation['properties']['manager']= UserSerializer(instance.manager).data
            representation['properties']['deputy']= UserSerializer(instance.deputy).data
            representation['properties']['assistant']= UserSerializer(instance.assistant).data
            representation['properties']['staff']= UserSerializer(instance.staff.all(), many=True).data
            representation['properties']['img_banner']= ImageSerializer(instance.img_banner).data
            representation['properties']['img_card']= ImageSerializer(instance.img_card).data
            representation['properties']['facility_type']= self.get_facility_type(instance)
            return representation
        return super().to_representation(instance)

    def create(self, validated_data):
        staff_ids = validated_data.pop('staff')
        instance = super().create(validated_data)
        print(f'DEBUG: Facility name: {instance.name}')
        print(f'DEBUG update staff_ids: {staff_ids}')
        print(f'DEBUG: {instance}')
        instance.staff.set(staff_ids)
        #if staff_ids:
        #    instance.staff.set(staff_ids)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        staff_ids = validated_data.pop('staff', [])
        instance = super().update(instance, validated_data)
        instance.staff.set(staff_ids)
        # if staff_ids:
        #     instance.staff.set(staff_ids)
        instance.save()
        return instance