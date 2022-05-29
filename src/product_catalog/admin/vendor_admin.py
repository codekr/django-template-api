from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from import_export.admin import ImportExportModelAdmin

from ..models import Vendor, VendorBrand


class VendorBrandInline(admin.TabularInline):
    model = VendorBrand
    autocomplete_fields = ['brand']
    max_num = 1


@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    inlines = [VendorBrandInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Vendor Quickbook", {
            'fields': (
                'qb_id',
            ),
        }),
        ("Vendor Name", {
            'fields': (
                'company_name',
            ),
        }),
        ("Vendor Address", {
            'fields': (
                ('address', 'address2',),
                'city',
                'zip_pin_code'
            ),
        }),
    )
    list_display = (
        'vendor_id', 'qb_id', 'company_name',
        'address', 'address2', 'city', 'zip_pin_code',
        'created_at', 'updated_at'
    )
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('qb_id',)
    search_fields = (
        'vendor_id', 'company_name', 'address', 'address2', 'city', 'zip_pin_code',)
    ordering = ('-updated_at',)
