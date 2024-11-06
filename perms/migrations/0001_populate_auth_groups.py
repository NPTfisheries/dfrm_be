from django.db import migrations
from django.contrib.auth.models import Group

def populate_groups(apps, schema_editor):
    # List of user roles to populate the Group table
    user_roles = ["Admin", "Manager", "Project_leader", "Professional", "Technician", "Guest"]
    
    # Iterate through each role and create it if it doesn't exist
    for role_name in user_roles:
        Group.objects.get_or_create(name=role_name)  # Creates the group if it doesn't exist

class Migration(migrations.Migration):
    dependencies = [
        ('sessions', '0001_initial'),  # Example auth migration
    ]
    
    operations = [
        migrations.RunPython(populate_groups),
    ]
