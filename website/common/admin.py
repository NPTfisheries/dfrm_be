from django.contrib import admin
from .models import ObjectLookUp

# Register your models here.
@admin.register(ObjectLookUp)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'object_type', 'name', 'created_at', 'updated_at', 'is_active')