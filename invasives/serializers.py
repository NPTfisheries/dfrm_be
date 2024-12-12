from rest_framework import serializers
from .models import InvasiveSpecies

class InvasiveSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvasiveSpecies
        fields = '__all__'
