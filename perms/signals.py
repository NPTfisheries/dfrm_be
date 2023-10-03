#perms/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User
from django.contrib.auth.models import Group

# @receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    print(type(instance.role))
    
    if type(instance.role) == str:
        role = int(instance.role)
    else:
        role = instance.role

    if created:
        if role == 1:
            group = Group.objects.get(name='Admin')
            instance.is_staff = True
            instance.save()
        elif role == 2:
            group = Group.objects.get(name='Manager')
        elif role == 3:
            group = Group.objects.get(name='Project_leader')
        elif role == 4:
            group = Group.objects.get(name="Professional")
        elif role == 5:
            group = Group.objects.get(name='Technician')
        else:
            group = None
        if group:
            instance.groups.add(group)