from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission

# def populate_groups(apps, schema_editor):

# # Create user groups
#     user_roles = ["Admin", "Manager", "Professional", "Technician", "Guest"]
#     for name in user_roles:
#         Group.objects.create(name=name)

#     # Permissions have to be created before applying them
#     for app_config in apps.get_app_configs():
#         app_config.models_module = True
#         create_permissions(app_config, verbosity=0)
#         app_config.models_module = None

#     # Assign model-level permissions to Admin 
#     all_perms = Permission.objects.all()
#     admin_perms = [i for i in all_perms if i.content_type.app_label == "administration"]
#     Group.objects.get(name="Admin").permissions.add(*admin_perms)

def populate_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Define role-specific permissions by app and model
    role_permissions = {
        "Admin": {
            "account.User": ["view", "add", "change", "delete"],
            "account.Profile": ["view", "add", "change", "delete"],      
            "administration.Department": ["view", "add", "change", "delete"],
            "administration.Division": ["view", "add", "change", "delete"],
            "administration.Project": ["view", "add", "change", "delete"],
            "administration.Subproject": ["view", "add", "change", "delete"],
            "administration.Task": ["view", "add", "change", "delete"],
            "files.Image": ["view", "add", "change", "delete"],
        },
        "Manager": {
            "account.User": ["view", "change"],
            "account.Profile": ["view", "change"],      
            "administration.Department": ["view", "add", "change"],
            "administration.Division": ["view", "add", "change"],
            "administration.Project": ["view", "add", "change"],
            "administration.Subproject": ["view", "add", "change"],
            "administration.Task": ["view", "add", "change"],
            "files.Image": ["view", "add", "change"],
        },
        "Professional": {
            "account.User": ["view", "change"],
            "account.Profile": ["view", "change"],  
            "administration.Department": ["view"],
            "administration.Division": ["view"],
            "administration.Project": ["view", "add", "change"],
            "administration.Subproject": ["view", "add", "change"],
            "administration.Task": ["view", "add", "change"],
            "files.Image": ["view", "add", "change"],
        },
        "Technician": {
            "account.User": ["view", "change"],
            "account.Profile": ["view", "change"], 
            "administration.Department": ["view"],
            "administration.Division": ["view"],
            "administration.Project": ["view"],
            "administration.Subproject": ["view"],
            "administration.Task": ["view"],
            "files.Image": ["view"],
        },
        "Guest":  {
            "account.User": ["view"],
            "account.Profile": ["view"],
            "administration.Department": ["view"],
            "administration.Division": ["view"],
            "administration.Project": ["view"],
            "administration.Subproject": ["view"],
            "administration.Task": ["view"],
            "files.Image": ["view"],
        }
    }

    for role_name, model_permissions in role_permissions.items():
        group, created = Group.objects.get_or_create(name=role_name)

        for model, permissions in model_permissions.items():
            for codename in permissions:
                permission = Permission.objects.get(codename=codename, content_type__model=model.lower())
                group.permissions.add(permission)