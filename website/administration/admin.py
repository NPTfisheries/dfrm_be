from django.contrib.gis import admin
from guardian.admin import GuardedModelAdmin
from administration.models import Department, Division, Project, Subproject, ObjectLookUp, Task, Facility
# Register your models here.

@admin.register(Department)
class DepartmentClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'deputy', 'assistant', 'slug', 'created_at', 'updated_at', 'is_active')

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'deputy', 'assistant', 'slug', 'created_at', 'updated_at', 'is_active')

@admin.register(Project)
class ProjectAdmin(GuardedModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at', 'is_active')

@admin.register(Subproject)
class SubprojectAdmin(GuardedModelAdmin):
    list_display = ('id', 'name', 'slug', 'lead', 'project', 'created_at', 'updated_at', 'is_active')

@admin.register(Task)
class TaskAdmin(GuardedModelAdmin):
    list_display = ('id', 'task_type', 'subproject', 'supervisor', 'created_at', 'updated_at', 'is_active')

@admin.register(Facility)
class FacilityAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'facility_type', 'name', 'coordinates', 'created_at', 'updated_at', 'is_active')