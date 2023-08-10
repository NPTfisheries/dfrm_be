# Generated by Django 4.2.4 on 2023-08-08 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_remove_department_img_banner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_project', to='administration.project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='subproject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_subprojects', to='administration.subproject'),
        ),
    ]