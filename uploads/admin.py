from django.contrib import admin
from .models import Upload
# Register your models here.

# How to format an admin view
class UploadAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'upload_at']

admin.site.register(Upload, UploadAdmin)

