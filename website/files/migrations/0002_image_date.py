# Generated by Django 4.2.4 on 2023-08-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateField(default='1900-01-01'),
        ),
    ]