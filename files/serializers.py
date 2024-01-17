#files/serializers.py
from rest_framework import serializers
from account.models import User
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import Permission
from files.models import Image, Document
from common.serializers import BaseModelSerializer, MetaModelSerializer
from account.serializers import UserSerializer


class ImageSerializer(BaseModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'slug', 'name', 'description', 'photographer', 'photo_date', 'source', 'image']

    def create(self, validated_data):
        user = self.context['request'].user
        instance = super().create(validated_data)
        perm = Permission.objects.get(codename='change_image')
        assign_perm(perm, user, instance)
        
        delete_perm = Permission.objects.get(codename='delete_image')
        assign_perm(delete_perm, user, instance)

        instance.save()
        return instance

class DocumentSerializer(MetaModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'document', 'title', 'description', 'primary_author', 'employee_authors', 'publish_date', 'document_type', 'citation', 'keywords']
    
    def to_representation(self, instance):
        # Override field representation for GET requests
        if self.context['request'].method == 'GET':
            return {
                **super().to_representation(instance),
                'employee_authors': UserSerializer(instance.employee_authors.all(), many=True).data
            }
        return super().to_representation(instance)
        
    def create(self, validated_data):
        user = self.context['request'].user
        ids = validated_data.pop('employee_authors')
        instance = super().create(validated_data)
        instance.employee_authors.set(ids)

        perm = Permission.objects.get(codename='change_document')
        assign_perm(perm, user, instance)

        delete_perm = Permission.objects.get(codename='delete_document')
        assign_perm(delete_perm, user, instance)

        instance.save()
        return instance


    def update(self, instance, validated_data):
        if 'employee_authors' in  validated_data:
            ids = validated_data.pop('employee_authors')
            instance.employee_authors.set(ids)
        instance = super().update(instance, validated_data)
        return instance
