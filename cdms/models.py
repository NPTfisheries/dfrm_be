from django.db import models
from common.models import MetaModel
from account.models import User
from administration.models import Project

class Location(MetaModel):
    class Meta:
        abstract = True
        ordering = ['name']
    name = models.CharField(max_length=300)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.IntegerField()
    river_kilometer = models.FloatField()
    projection = models.CharField(max_length=100)
    # sde_feature_class_id
    # timezone

class Dataset(MetaModel):
    class Meta:
        abstract = True
        ordering = ['name']
    name = models.CharField(max_length=300)
    description = models.TextField()

class Instrument(MetaModel):
    class Meta:
        abstract = True
        ordering = ['name']
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=300)
    description = models.TextField()
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)

class Activity(MetaModel):   # this will have "is_active"
    class Meta:
        abstract = True
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    project = models.ForeignKey(Project)
    dataset = models.ForeignKey(Dataset)
    instrument = models.ForeignKey(Instrument)
    date = models.DateField()
    # data

# we need to include everything needed for ag grid, and replicate here.
class Field(MetaModel):
    class Meta:
        abstract = True
    dataset = models.ForeignKey(Dataset)