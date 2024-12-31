from django.db import models
from django.contrib.gis.db import models as gis_models
from common.models import MetaModel

class Location(MetaModel):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField(null=True, blank=True)
    geometry = gis_models.GeometryField(srid=4326) # WGS84
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
