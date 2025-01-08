from django.db import models
from common.models import ObjectLookUp
import os
from common.utils import delete_file, delete_s3_object
# Create your models here.

class InvasiveSpecies(models.Model):  
    common_name = models.CharField(max_length=300)
    species_name = models.CharField(max_length=300)
    species_image = models.ImageField(upload_to='images/invasives/')
    image_attribution = models.TextField(null=True, blank=True, help_text='Include the entire url [ https://www.nezperce.org ].  If using an NPT photo, you may leave blank.')
    image1 =  models.ImageField(upload_to='images/invasives/') 
    image1_attribution = models.TextField(null=True, blank=True, help_text='Include the entire url [ https://www.nezperce.org ].  If using an NPT photo, you may leave blank.')
    image2 =  models.ImageField(upload_to='images/invasives/') 
    image2_attribution = models.TextField(null=True, blank=True, help_text='Include the entire url [ https://www.nezperce.org ].  If using an NPT photo, you may leave blank.')
    description = models.TextField(null=True, blank=True)
    size = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    shape = models.TextField(null=True, blank=True)
    habitat = models.TextField(null=True, blank=True)
    native_to = models.TextField(null=True, blank=True)
    invasive_type = models.ForeignKey(ObjectLookUp, null=True, on_delete=models.PROTECT, limit_choices_to={'object_type': 'Invasive'}, related_name="%(class)s_object_lookups")
    sort_order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.common_name;

    class Meta:
        verbose_name = 'Invasive Species'
        verbose_name_plural = 'Invasive Species'

    def _delete_image(self, image_field):
        mode = os.getenv('MODE') 

        """
        Deletes the given image file from the storage backend (local or S3).
        """
        if mode == 'Prod':  
            delete_s3_object(image_field.name)  # Deletes from S3
        else:
            delete_file(image_field.path)  # Dev
