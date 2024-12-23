# Generated by Django 4.2.4 on 2024-12-23 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvasiveSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=300)),
                ('species_name', models.CharField(max_length=300)),
                ('species_image', models.ImageField(upload_to='images/invasives/')),
                ('image_attribution', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(upload_to='images/invasives/')),
                ('image1_attribution', models.TextField(blank=True, null=True)),
                ('image2', models.ImageField(upload_to='images/invasives/')),
                ('image2_attribution', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('size', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('shape', models.TextField(blank=True, null=True)),
                ('habitat', models.TextField(blank=True, null=True)),
                ('native_to', models.TextField(blank=True, null=True)),
                ('sort_order', models.IntegerField(default=1)),
                ('invasive_type', models.ForeignKey(limit_choices_to={'object_type': 'Invasive'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_object_lookups', to='common.objectlookup')),
            ],
            options={
                'verbose_name': 'Invasive Species',
                'verbose_name_plural': 'Invasive Species',
            },
        ),
    ]
