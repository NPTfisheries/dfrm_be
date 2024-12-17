from django.db import models
from common.models import ObjectLookUp
import os
from common.utils import delete_file, delete_s3_object
# Create your models here.

class InvasiveSpecies(models.Model):  
    common_name = models.CharField(max_length=300)
    species_name = models.CharField(max_length=300)
    species_image = models.ImageField(upload_to='images/invasives/')
    image_attribution = models.TextField(null=True)
    map_image =  models.ImageField(upload_to='images/invasives/', help_text="Map image must be a screenshot from https://nas.er.usgs.gov/viewer/omap.aspx") # testing
    description = models.TextField(null=True)
    size = models.TextField(null=True)
    color = models.TextField(null=True)
    shape = models.TextField(null=True)
    habitat = models.TextField(null=True)
    native_to = models.TextField(null=True)
    invasive_type = models.ForeignKey(ObjectLookUp, null=True, on_delete=models.PROTECT, limit_choices_to={'object_type': 'Invasive'}, related_name="%(class)s_object_lookups")
    sort_order = models.IntegerField(default=1)

    def __str__(self):
        return self.common_name;

    class Meta:
        verbose_name = 'Invasive Species'
        verbose_name_plural = 'Invasive Species'

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = InvasiveSpecies.objects.get(pk=self.pk)

            # Handle species_image replacement
            if old_instance.species_image and old_instance.species_image != self.species_image:
                self._delete_image(old_instance.species_image)

            # Handle map_image replacement
            if old_instance.map_image and old_instance.map_image != self.map_image:
                self._delete_image(old_instance.map_image)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete associated images
        if self.species_image:
            self._delete_image(self.species_image)
        if self.map_image:
            self._delete_image(self.map_image)

        super().delete(*args, **kwargs)

    def _delete_image(self, image_field):
        """
        Delete an image, either locally or from S3 depending on the environment.
        """
        image_path = image_field.path  # Local filesystem path
        image_name = image_field.name  # Relative path used as S3 object key

        mode = os.getenv('MODE') 

        if mode == 'Dev':  # Development mode
            delete_file(image_path)
        else:  # Production mode
            delete_s3_object(image_name)
