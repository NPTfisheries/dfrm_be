from django.contrib import admin
from invasives.models import InvasiveSpecies

# Register your models here.
@admin.register(InvasiveSpecies)
class InvasivesClassAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'species_name', 'species_image', 'image_attribution', 'description', 'size', 'color', 'shape', 'habitat', 'native_to', 'invasive_type', 'sort_order', 'map_image')