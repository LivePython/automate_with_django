from django.contrib import admin
from .models import CompressImage
from django.utils.html import format_html  # This is use to work wit html tags in functions in django


class CompressImageAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.compressed_image.url}" width="40" height="40">')
    
    def original_image_size(self, obj):
        size_in_mb = obj.original_img.size / (1024 * 1024)  # Keep as a numeric value
        if size_in_mb > 1:
            return format_html(f'{size_in_mb:.2f} Mb')
        else:
            size_in_kb = obj.original_img.size / 1024
            return format_html(f'{size_in_kb:.2f} kb')
        
    def compressed_image_size(self, obj):
        size_in_mb = obj.compressed_image.size / (1024*1024)
        if size_in_mb > 1:
            return format_html(f'{size_in_mb:.2f} Mb')
        else:
            size_in_kb = obj.compressed_image.size / 1024
            return format_html(f'{size_in_kb:.2f} kb')
        
        
        
    list_display = ('user', 'thumbnail','original_image_size', 'compressed_image_size', 'compressed_at')
    
    
admin.site.register(CompressImage, CompressImageAdmin)

# Register your models here.
