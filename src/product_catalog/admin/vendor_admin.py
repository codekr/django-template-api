from django.contrib import admin
from django.db import models
from django.forms import Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Vendor


@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Vendor Form", {
            'fields': (
                'qb_id',
                'company_name',
                'address',
                ('address2', 'city', 'zip_pin_code',),
            ),
        }),
    )
    list_display = (
        'vendor_id', 'company_name', 'qb_id',
        'address', 'address2', 'city', 'zip_pin_code',
        'created_at', 'updated_at'
    )
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('qb_id',)
    search_fields = (
        'vendor_id', 'company_name', 'address', 'address2', 'city', 'zip_pin_code',)
    ordering = ('updated_at',)
