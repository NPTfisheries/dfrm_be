# Generated by Django 4.2.4 on 2023-08-07 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_department_slug_division_slug_project_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='division',
            name='staff',
        ),
    ]
