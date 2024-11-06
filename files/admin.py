from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from files.models import Image, Document
# Register your models here.

@admin.register(Image)
class ImageClassAdmin(GuardedModelAdmin):
    list_display = ('id','created_at', 'updated_at', 'created_by', 'name')

@admin.register(Document)
class DocumentClassAdmin(GuardedModelAdmin):
    list_display = ('id', 'title', 'document_type', 'description', 'primary_author', 'publish_date')