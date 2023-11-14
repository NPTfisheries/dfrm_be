from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from files.models import Image, Document
# Register your models here.

@admin.register(Image)
class DepartmentClassAdmin(admin.ModelAdmin):
    list_display = ('id','created_at', 'updated_at', 'created_by', 'name')

@admin.register(Document)
class SubprojectAdmin(GuardedModelAdmin):
    list_display = ('id', 'title', 'description', 'primary_author', 'publish_date')