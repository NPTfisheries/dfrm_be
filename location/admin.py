from django.contrib import admin
from django.contrib.gis import admin
from location.models import Location

@admin.register(Location)
class LocationAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'description', 'elevation', 'river_kilometer', 'geom')

