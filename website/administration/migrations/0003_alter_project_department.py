# Generated by Django 4.2.4 on 2023-08-16 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_project_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_department', to='administration.department'),
        ),
    ]