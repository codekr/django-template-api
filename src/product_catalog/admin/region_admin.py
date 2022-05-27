from django.contrib import admin
from src.product_catalog.models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'region_id', 'region_name', 'region_description',
        'display_order', 'is_approved', 'created_at', 'updated_at'
    )
    list_select_related = ('image',)
    list_filter = ('created_at', 'updated_at', 'region_name')
    search_fields = ('brand_id', 'region_name',)
    autocomplete_fields = ('image',)
    ordering = ('updated_at',)
