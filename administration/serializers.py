from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from guardian.shortcuts import assign_perm, remove_perm
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
        fields = ['id', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card', 'is_active', 'display']


class DivisionSerializer(BaseAdminSerializer):
    class Meta:
        model = Division
        fields = ['id', 'department', 'slug', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card', 'is_active', 'display']


class ProjectSerializer(BaseModelSerializer):
    project_leader = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Project
        fields = ['id', 'department', 'slug', 'name', 'description', 'project_leader', 'img_banner', 'img_card', 'is_active', 'display']

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
        for id in ids:
            assign_perm(perm, id, instance)
        instance.project_leader.set(ids)
        return instance

    def update(self, instance, validated_data):
        new_pls = validated_data.pop('project_leader', [])
        perm = Permission.objects.get(codename='change_project')

        old_pls = instance.project_leader.all()
        for pl in old_pls:
            if pl != instance.created_by:
                remove_perm(perm, pl, instance)

        for new_pl in new_pls:
            assign_perm(perm, new_pl, instance)  # editors

        instance = super().update(instance, validated_data)
        instance.project_leader.set(new_pls)
        instance.save()
        return instance

class TaskSerializer(MetaModelSerializer):    
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'task_type', 'division', 'project', 'supervisor', 'img_banner', 'img_card', 'sort_order', 'is_active', 'editors', 'allowed_access', 'display']

    def get_task_type(self, instance):
        return ObjectLookUpSerializer(instance.task_type).data;

    def create(self, validated_data):
        user = self.context['request'].user
        ids = validated_data.pop('editors')
        instance = super().create(validated_data)
        perm = Permission.objects.get(codename='change_task')
        assign_perm(perm, user, instance)  # user who creates
        assign_perm(perm, instance.supervisor, instance) # user who is supervisor
        for id in ids:
            assign_perm(perm, id, instance)  # editors
        instance.editors.set(ids)

        return instance

    def update(self, instance, validated_data):
        new_editors = validated_data.pop('editors', [])
        perm = Permission.objects.get(codename='change_task')
        # remove existing perms, but not if they're creator
        old_editors = instance.editors.all()
        for editor in old_editors:
            if editor != instance.created_by:
                remove_perm(perm, editor, instance)
        
        assign_perm(perm, instance.supervisor, instance) # user who is supervisor
        for new_editor in new_editors:
            assign_perm(perm, new_editor, instance)

        instance = super().update(instance, validated_data)
        instance.editors.set(new_editors)
        instance.save()
        return instance
    
class TaskDetailSerializer(MetaModelSerializer):  # GET
    editors = UserSerializer(many=True)
    supervisor = UserSerializer()
    img_card = ImageSerializer()
    img_banner = ImageSerializer()

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'task_type', 'division', 'project', 'supervisor', 'img_banner', 'img_card', 'sort_order', 'is_active', 'editors', 'allowed_access', 'display']
        depth = 1  

    def get_task_type(self, instance):
        return ObjectLookUpSerializer(instance.task_type).data
    


class FacilitySerializer(BaseModelSerializer, GeoFeatureModelSerializer):
   
    class Meta:
        model = Facility
        fields = ['id', 'slug', 'facility_type', 'name', 'description', 'manager', 'deputy', 'assistant', 'staff', 'img_banner', 'img_card', 'facility_type', 'phone_number', 'street_address', 'mailing_address', 'city', 'state', 'zipcode', 'is_active', 'display']
        geo_field = 'geometry'

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