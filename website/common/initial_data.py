from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission

def populate_groups(apps, schema_editor):
# """
# This function is run in migrations/0002_initial_data.py as an initial
# data migration at project initialization. it sets up some basic model-level
# permissions for different groups when the project is initialised.

# Maintainer: Full permissions over the batteryDB app to add, change, delete, view
# data in the database, but not users.
# Read only: Not given any initial permissions. View permission is handled on a
# per instance basis by Django Guardian (more on that later!).
# """

# Create user groups
    user_roles = ["Admin", "Manager", "Professional", "Technician", "Guest"]
    for name in user_roles:
        Group.objects.create(name=name)

    # Permissions have to be created before applying them
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None

    # Assign model-level permissions to Admin 
    all_perms = Permission.objects.all()
    admin_perms = [i for i in all_perms if i.content_type.app_label == "administration"]
    Group.objects.get(name="Admin").permissions.add(*admin_perms)