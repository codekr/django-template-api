from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from import_export.admin import ImportExportModelAdmin

from ..models import VendorBrand


@admin.register(VendorBrand)
class VendorBrandAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        (None, {
            'fields': (
                'brand',
                'vendor',
            ),
        }),
    )
    list_display = (
        'vendor_brand_id', 'brand', 'vendor', 'created_at', 'updated_at'
    )
    list_display_links = ('brand', 'vendor',)
    list_filter = ('updated_at',)
    list_select_related = ('brand', 'vendor',)
    autocomplete_fields = ('brand', 'vendor',)
    search_fields = (
        'vendor_brand_id', 'brand__brand_name', 'vendor__company_name')
    ordering = ('-updated_at',)
