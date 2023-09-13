# Generated by Django 4.2.4 on 2023-09-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Manager'), (3, 'Project_leader'), (4, 'Professional'), (5, 'Technician'), (6, 'Guest')], default=5),
        ),
    ]
