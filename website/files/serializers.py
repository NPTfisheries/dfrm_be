#files/serializers.py
from rest_framework import serializers
from account.models import User
from files.models import Image
from common.serializers import BaseModelSerializer


class ImageSerializer(BaseModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'slug', 'name', 'description', 'photographer', 'photo_date', 'source', 'image']