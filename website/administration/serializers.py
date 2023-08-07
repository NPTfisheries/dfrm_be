#admin/serializers.py
from rest_framework import serializers
from administration.models import Department, Division, Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'description', 'manager', 'deputy', 'assistant', 'img_banner', 'img_card']
        lookup_field = 'slug'
        extra_kwargs = {
            'extra_kwargs':{'created_by':{'read_only':True}, 'updated_by':{'read_only':True}},
            'url':{'lookup_field':'slug'}
        }

    def create(self, validated_data):
        # get authenticated user
        user = self.context['request'].user
        if user.is_staff:
            # create a new instance
            instance = Department(**validated_data)

            instance.created_by = user
            instance.updated_by = user
            instance.is_active = True
            
            instance.save()

            return instance
        else:
            raise serializers.ValidationError({"authorize": "You don't have permission for this action."})

    def update(self, instance, validated_data):
        # get authenticated user
        user = self.context['request'].user
        # check if authenticated user is equal to the user instance being modified
        if user.is_staff or user == instance.manager or user == instance.deputy or user == instance.assistant:
            # Update the Profile model instance with the values supplied in the request.
            for field, value in validated_data.items():
                setattr(instance, field, value)

            instance.updated_by = user
            instance.save()

            return instance

        else:
            raise serializers.ValidationError({"authorize": "You don't have permission for this action."})

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'