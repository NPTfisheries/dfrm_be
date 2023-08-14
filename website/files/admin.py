from django.contrib import admin
from files.models import Image
# Register your models here.

@admin.register(Image)
class DepartmentClassAdmin(admin.ModelAdmin):
    list_display = ('id','created_at', 'updated_at', 'created_by', 'name')
