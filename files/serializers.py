#files/serializers.py
from rest_framework import serializers
from account.models import User
from files.models import Image, Document
from common.serializers import BaseModelSerializer, MetaModelSerializer
from account.serializers import UserSerializer


class ImageSerializer(BaseModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'slug', 'name', 'description', 'photographer', 'photo_date', 'source', 'image']

class DocumentSerializer(MetaModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'file', 'title', 'description', 'primary_author', 'employee_authors', 'publish_date', 'file_type', 'citation', 'keywords']

    def to_representation(self, instance):
        # Override field representation for GET requests
        if self.context['request'].method == 'GET':
            return {
                **super().to_representation(instance),
                'employee_authors': UserSerializer(instance.employee_authors.all(), many=True).data
            }
        return super().to_representation(instance)

    def create(self, validated_data):
        ids = validated_data.pop('employee_authors')
        instance = super().create(validated_data)
        instance.employee_authors.set(ids)
        return instance

    def update(self, instance, validated_data):
        if 'employee_authors' in  validated_data:
            ids = validated_data.pop('employee_authors')
            instance.employee_authors.set(ids)
        instance = super().update(instance, validated_data)
        return instance
