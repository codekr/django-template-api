from django.contrib import admin
from src.product_catalog.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'item_id', 'item_name', 'item_alternate_name',
        'is_approved', 'created_at', 'updated_at'
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('item_id', 'item_name', 'item_alternate_name',)
    ordering = ('updated_at',)
