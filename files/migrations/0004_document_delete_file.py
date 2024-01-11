# Generated by Django 4.2.4 on 2023-11-13 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0003_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('document', models.FileField(editable=False, upload_to='documents/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('primary_author', models.CharField(max_length=50)),
                ('publish_date', models.DateField()),
                ('document_type', models.CharField(choices=[('Annual Report', 'Annual Report'), ('Journal Article', 'Journal Article'), ('Technical Memo', 'Technical Memo'), ('Presentation Slides', 'Presentation Slides'), ('Other', 'Other')], max_length=50)),
                ('citation', models.TextField(null=True)),
                ('keywords', models.CharField(max_length=100, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL)),
                ('employee_authors', models.ManyToManyField(related_name='%(app_label)s_%(class)s_employee_authors', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_editor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]