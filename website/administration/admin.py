from django.contrib import admin
from administration.models import Department, Division, Project
# Register your models here.

@admin.register(Department)
class DepartmentClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'deputy_manager', 'administrative_assistant')

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director', 'deputy_director', 'administrative_assistant')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')