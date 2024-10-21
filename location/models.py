from django.db import models
from django.contrib.gis.db import models as gis_models
from common.models import MetaModel

class Location(MetaModel):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField(null=True, blank=True)
    elevation = models.IntegerField(null=True, blank=True)
    river_kilometer = models.FloatField(null=True, blank=True)
    geom = gis_models.GeometryField(srid=4236) # WGS84
    # timezone
    # image ??

    def __str__(self):
        return self.name