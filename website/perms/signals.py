#perms/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    if created:
        if instance.role == 1:
            group = Group.objects.get(name='Admin')
            instance.is_staff = True
            instance.save()
        elif instance.role == 2:
            group = Group.objects.get(name='Manager')
        elif instance.role == 3:
            group = Group.objects.get(name='Project_leader')
        elif instance.role == 4:
            group = Group.objects.get(name="Professional")
        elif instance.role == 5:
            group = Group.objects.get(name='Technician')
        else:
            group = None
        if group:
            instance.groups.add(group)