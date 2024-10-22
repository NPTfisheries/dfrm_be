from django.contrib import admin
from django.contrib.gis import admin
from location.models import Location

@admin.register(Location)
class LocationAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = { 'attrs': 
                    { 'default_lon':-116.087802, 'default_lat': 45.25, 'default_zoom': 5,
                    }
                    }        
    list_display = ('name', 'description', 'geometry')

