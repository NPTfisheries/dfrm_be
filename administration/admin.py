from django.contrib.gis import admin
from guardian.admin import GuardedModelAdmin
from administration.models import Department, Division, Project, Task, Facility
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

@admin.register(Task)
class TaskAdmin(GuardedModelAdmin):
    list_display = ('id', 'name', 'task_type', 'division', 'project', 'supervisor', 'created_at', 'updated_at', 'is_active')

@admin.register(Facility)
class FacilityAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'facility_type', 'name', 'coordinates', 'created_at', 'updated_at', 'is_active')