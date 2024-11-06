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
    list_display = ('id', 'name', 'task_type', 'division', 'project', 'supervisor', 'created_at', 'updated_at', 'is_active', 'allowed_access')

@admin.register(Facility)
class FacilityAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = { 'attrs': 
                { 'default_lon':-116.087802, 'default_lat': 45.25, 'default_zoom': 5,
                }
                }   
    list_display = ('id', 'facility_type', 'name', 'geometry', 'created_at', 'updated_at', 'is_active')
    