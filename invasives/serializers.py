from rest_framework import serializers
from .models import InvasiveSpecies

class InvasiveSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvasiveSpecies
        fields = '__all__'
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # this makes sure the filepath is returned similar to any other to_representation request (project, user, dept, etc.)
        if instance.species_image:
            representation['species_image'] = f'/media/{instance.species_image}'
        if instance.image1:
            representation['image1'] = f'/media/{instance.image1}'
        if instance.image1:
            representation['image2'] = f'/media/{instance.image2}'
        return representation