#accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    if created:
        if instance.role == 1:
            group = Group.objects.get(name='Admin')
        elif instance.role == 2:
            group = Group.objects.get(name='Manager')
        elif instance.role == 3:
            group = Group.objects.get(name='Professional')
        elif instance.role == 4:
            group = Group.objects.get(name='Technician')
        else:
            group = Group.objects.get(name='Guest')
        
        instance.groups.add(group)