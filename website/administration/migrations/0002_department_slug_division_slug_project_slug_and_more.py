# Generated by Django 4.2.4 on 2023-08-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='division',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='subproject',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
