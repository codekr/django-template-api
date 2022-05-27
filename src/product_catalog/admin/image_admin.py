from django.contrib import admin
from src.product_catalog.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'image_id', 'filename', 'alt_text',
        'storage_id', 'type', 'created_at', 'updated_at'
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('image_id', 'filename', 'alt_text',)
    ordering = ('updated_at',)
