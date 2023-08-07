from django.contrib import admin
from administration.models import Department, Division, Project, Subproject, Task
# Register your models here.

@admin.register(Department)
class DepartmentClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'deputy', 'assistant', 'slug', 'created_at', 'updated_at')

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'deputy', 'assistant', 'slug')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')

@admin.register(Subproject)
class SubprojectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')