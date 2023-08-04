# Generated by Django 4.2.4 on 2023-08-04 21:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administration', '0003_remove_department_is_active_division'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='division',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='department',
            name='banner',
            field=models.ImageField(default='images/wallowalake.JPG', upload_to='images/department/', verbose_name='Department Banner'),
        ),
        migrations.AlterField(
            model_name='division',
            name='banner',
            field=models.ImageField(default='images/wallowalake.JPG', upload_to='images/division/', verbose_name='Division Banner'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Project Name')),
                ('description', models.TextField(verbose_name='Project Description')),
                ('created', models.DateTimeField(verbose_name='Project Created')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Project (check for yes)')),
                ('project_image1', models.ImageField(default='images/wallowalake.JPG', upload_to='images/project/', verbose_name='Project Banner')),
                ('project_leader', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Project Leader')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
