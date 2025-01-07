from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

def populate_group_permissions(apps, schema_editor):

    role_permissions = {
        "Admin": {
            'account': {
                'user': ["view", "add", "change", "delete"],
                'profile': ["view", "add", "change", "delete"],
            },
            'administration': {
                'department': ["view", "add", "change", "delete"],
                'division': ["view", "add", "change", "delete"],
                'project': ["view", "add", "change", "delete"],
                'task': ["view", "add", "change", "delete"],
                'facility': ["view", "add", "change", "delete"],
            },
            'files': {
                'image': ["view", "add", "change", "delete"],
                'document': ["view", "add", "change", "delete"],
            },
            'location': {
                'location': ["view", "add", "change", "delete"]
            }
        },
        "Manager":{
            'account':{
                'user':["view", "change"],
                'profile':["view", "change"]
            },
            'administration':{
                'department':["view", "change"],
                'division':["view", "change"],
                'project':["view","add","change"],
                'task':["view","add","change"],
                'facility':["view", "add", "change"],
            },
            'files':{
                'image':["view","add","change","delete"],
                'document':["view","add","change","delete"]
            },
            'location': {
                'location': ["view", "add", "change"]
            }
        },
        "Project_leader":{
            'account':{
                'user':["view","change"],
                'profile':["view", "change"]
            },
            'administration':{
                'department':["view"],
                'division':["view"],
                'project':["view","add","change"],
                'task':["view","add","change"],
                'facility':["view"],
            },
            'files':{
                'image':["view", "add", "change","delete"],
                'document':["view","add","change","delete"]
            },
            'location': {
                'location': ["view", "add", "change"]
            }
        },
        "Professional":{
            'account':{
                'user':["view","change"],
                'profile':["view", "change"]
            },
            'administration':{
                'department':["view"],
                'division':["view"],
                'project':["view", "change"],
                'task':["view", "change"],
                'facility':["view"],
            },
            'files':{
                'image':["view"],
                'document':["view","add","change","delete"]
            },
            'location': {
                'location': ["view"]
            }
        },
        "Technician":{
            'account':{
                'user':["view", "change"],
                'profile':["view", "change"]
            },
            'administration':{
                'department':["view"],
                'division':["view"],
                'project':["view"],
                'task':["view"],
                'facility':["view"],
            },
            'files':{
                'image':["view"],
                'document':["view"]
            },
            'location': {
                'location': ["view"]
            }
        },
        "Guest":{
            'account':{
                'user':["view"],
                'profile':["view"]
            },
            'administration':{
                'department':["view"],
                'division':["view"],
                'project':["view"],
                'task':["view"],
                'facility':["view"],
            },
            'files':{
                'image':["view"],
                'document':["view"]
            },
            'location': {
                'location': ["view"]
            }
        }  
    }

    for role_name, app_models in role_permissions.items():
        group = Group.objects.get(name=role_name)

        for app_label, models in app_models.items():
            for model_name, permissions in models.items():
                content_type = ContentType.objects.get(app_label=app_label, model=model_name)

                for permission_type in permissions:
                    codename = f"{permission_type}_{model_name}"
                    permission, created = Permission.objects.get_or_create(codename=codename, content_type=content_type)
                    group.permissions.add(permission)

class Migration(migrations.Migration):
    dependencies = [
        ('perms', '0001_populate_auth_groups'),  # Must run after the group creation migration
        ('contenttypes', '0002_remove_content_type_name')  # this dependency didn't fix. 10/2/24
    ]
    
    operations = [
        migrations.RunPython(populate_group_permissions),
    ]
