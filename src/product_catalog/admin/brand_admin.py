from django.contrib import admin
from src.product_catalog.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand_id', 'brand_name',
        'is_exclusive', 'is_recognised_brand', 'is_approved',
        'created_at', 'updated_at'
    )
    list_select_related = ('image',)
    list_filter = ('created_at', 'updated_at', 'brand_name')
    search_fields = ('brand_id', 'brand_name',)
    autocomplete_fields = ('image',)
    ordering = ('updated_at',)
