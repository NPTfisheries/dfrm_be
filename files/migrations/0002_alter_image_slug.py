# Generated by Django 4.2.4 on 2023-10-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
