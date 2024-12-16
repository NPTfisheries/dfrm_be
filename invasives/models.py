from django.db import models
from common.models import ObjectLookUp

# Create your models here.

class InvasiveSpecies(models.Model):  
    common_name = models.CharField(max_length=300)
    species_name = models.CharField(max_length=300)
    species_image = models.ImageField(null=True, upload_to='images/invasives/') # for testing
    image_attribution = models.TextField(null=True) # for testing
    description = models.TextField()
    size = models.TextField()
    color = models.TextField()
    shape = models.TextField()
    habitat = models.TextField()
    native_to = models.TextField()
    invasive_type = models.ForeignKey(ObjectLookUp, null=True, on_delete=models.PROTECT, limit_choices_to={'object_type': 'Invasive'}, related_name="%(class)s_object_lookups")
    sort_order = models.IntegerField(default=1)

    def __str__(self):
        return self.common_name;

    class Meta:
        verbose_name = 'Invasive Species'
        verbose_name_plural = 'Invasive Species'
