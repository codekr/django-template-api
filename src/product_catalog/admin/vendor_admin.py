from django.contrib import admin
from src.product_catalog.models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'vendor_id', 'qb_id', 'vendor_company_name',
        'vendor_address', 'vendor_address2', 'vendor_city', 'vendor_zip_pin_code',
        'created_at', 'updated_at'
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = (
        'vendor_id', 'vendor_company_name', 'vendor_address', 'vendor_address2', 'vendor_city', 'vendor_zip_pin_code',)
    ordering = ('updated_at',)
