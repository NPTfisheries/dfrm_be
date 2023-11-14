#from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def populate_groups(apps, schema_editor):

    user_roles = ["Admin", "Manager", "Project_leader", "Professional", "Technician", "Guest"]
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
                'facility':["view", "add", "change","delete"],
            },
            # 'common':{
            #     'objectlookup':["view","add","change","delete"],
            # },
            'files':{
                'image':["view","add","change","delete"],
                'document':["view","add","change","delete"]
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
                'subproject':["view","add","change"],
                'task':["view","add","change"],
                'facility':["view", "add", "change"],
            },
            'files':{
                'image':["view","add","change"],
                'document':["view","add","change"]
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
                'subproject':["view","add","change"],
                'task':["view","add","change"],
                'facility':["view"],
            },
            'files':{
                'image':["view", "add", "change"],
                'document':["view","add","change"]
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
                'subproject':["view", "change"],
                'task':["view", "change"],
                'facility':["view"],
            },
            'files':{
                'image':["view"],
                'document':["view","add","change"]
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
                'facility':["view"],
            },
            'files':{
                'image':["view"],
                'document':["view"]
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
                'facility':["view"],
            },
            'files':{
                'image':["view"],
                'document':["view"]
            }
        }  
    }

    for role_name, app in role_permissions.items():
        print(f"Role name: {role_name}")
        group = Group.objects.get(name = role_name)
        print(f"Group is: {group}")
        for app_label, model in app.items():
            print(f"App label: {app_label}")
            
            print("Available Content Types:")
            for content_type in ContentType.objects.all():
                print(content_type.app_label, content_type.model)

            for model_name, permissions in model.items():
                print(f"Model name: {model_name}")
                print(f"Attempting to get ContentType for app_label={app_label} and model={model_name}")
                content_type = ContentType.objects.get(app_label = app_label, model=model_name) #takes app_label and model
                print(f"Content type: {content_type}")
                print(f"Permissions: {permissions}")
                for permission in permissions:
                    print(f"Permission: {permission}")
                    codename = f"{permission}_{model_name}"
                    print(f"Codename is: {codename}")
                    #permission = Permission.objects.get(codename=codename)#, content_type=content_type) #codename = 'view_user' works
                    permission, created = Permission.objects.get_or_create(codename=codename, content_type = content_type)
                    group.permissions.add(permission)