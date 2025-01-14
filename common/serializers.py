#common/serializers.py
from rest_framework import serializers
from .models import ObjectLookUp

class MetaModelSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        extra_kwargs = {
            'created_by': {'read_only': True},
            'updated_by': {'read_only': True},
        }

    def create(self, validated_data):
        # get authenticated user
        user = self.context['request'].user
        
        # check if booleans have been provided, else set to True
        is_active = validated_data.pop('is_active', True)
        display = validated_data.pop('display', True)

        # create a new instance
        instance = self.Meta.model.objects.create(
            created_by=user,
            updated_by=user,
            is_active=is_active,
            display=display,
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

class BaseModelSerializer(MetaModelSerializer):
    class Meta:
        abstract = True
        extra_kwargs = {
            'slug': {'read_only': True},
            'url': {'lookup_field': 'slug'}
        }

    def validate_name(self, value):
        # Check if a model object with the same name already exists
        if self.instance is None or self.instance.name != value:
            if self.Meta.model.objects.filter(name=value).exists():
                raise serializers.ValidationError("A model object with this name already exists.")
        return value
    
class ObjectLookUpSerializer(MetaModelSerializer):
    class Meta:
        model = ObjectLookUp
        fields = ['id', 'object_type', 'name']