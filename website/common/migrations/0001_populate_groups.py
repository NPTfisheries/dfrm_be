# Generated by Django 4.2.4 on 2023-08-14 20:58

from django.db import migrations
from ..initial_data import populate_groups


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial')
    ]

    operations = [
        migrations.RunPython(populate_groups)
    ]
