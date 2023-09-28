from django.contrib import admin
from .models import ObjectLookUp

@admin.register(ObjectLookUp)
class ObjectLookUpAdmin(admin.ModelAdmin):
    list_display = ('id', 'object_type', 'name', 'created_at', 'updated_at', 'is_active')