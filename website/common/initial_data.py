#from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def populate_groups(apps, schema_editor):

    user_roles = ["Admin", "Manager", "Professional", "Technician", "Guest"]
    for role_name in user_roles:
        group, created = Group.objects.get_or_create(name=role_name)


    # Define role-specific permissions by app and model
    role_permissions = {
        "Admin":{
            'account':{
                'user':["view", "add", "change", "delete"],
                'profile':["view", "add", "change", "delete"]
            },
            'administration':{
                'department':["view","add","change","delete"],
                'division':["view","add","change","delete"],
                'project':["view","add","change","delete"],
                'subproject':["view","add","change","delete"],
                'task':["view","add","change","delete"],
            },
            'files':{
                'image':["view","add","change","delete"]
            }
        },
        "Manager":{
            'account':{
                'user':["view", "change"],
                'profile':["view", "change"]
            },
            'administration':{
                'department':["view","add","change"],
                'division':["view","add","change"],
                'project':["view","add","change"],
                'subproject':["view","add","change"],
                'task':["view","add","change"],
            },
            'files':{
                'image':["view","add","change"]
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
                'project':["view","add","change"],
                'subproject':["view","add","change"],
                'task':["view","add","change"],
            },
            'files':{
                'image':["view"]
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
                'subproject':["view"],
                'task':["view"],
            },
            'files':{
                'image':["view"]
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
                'subproject':["view"],
                'task':["view"],
            },
            'files':{
                'image':["view"]
            }
        }  
    }

    for role_name, app in role_permissions.items():
        print(f"Role name: {role_name}")
        group = Group.objects.get(name = role_name)
        print(f"Group is: {group}")
        for app_label, model in app.items():
            print(f"App label: {app_label}")
            for model_name, permissions in model.items():
                print(f"Model name: {model_name}")
                #content_type = ContentType.objects.get(app_label = app_label, model=model_name) #takes app_label and model
                print(f"Permissions: {permissions}")
                for permission in permissions:
                    print(f"Permission: {permission}")
                    codename = f"{permission}_{model_name}"
                    print(f"Codename is: {codename}")
                    permission = Permission.objects.get(codename=codename)#, content_type=content_type) #codename = 'view_user' works
                    group.permissions.add(permission)