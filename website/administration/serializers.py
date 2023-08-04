#admin/serializers.py
from rest_framework import serializers
from administration.models import Department, Division, Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def update(self, instance, validated_data):
        # get authenticated user
        user = self.context['request'].user
        # check if authenticated user is equal to the user instance being modified
        if user.is_staff or user == instance.manager or user == instance.deputy_manager or user == instance.administrative_assistant:
            # Update the Profile model instance with the values supplied in the request.
            for field, value in validated_data.items():
                setattr(instance, field, value)

            instance.save()

            return instance

        else:
            raise serializers.ValidationError({"authorize": "You dont have permission to edit this information."})

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'