from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Brand, VendorBrand
from ..resources import BrandResource


class BrandVendorInline(admin.TabularInline):
    model = VendorBrand
    autocomplete_fields = ['vendor']
    max_num = 1


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource
    actions = ['mark_approved', 'unmark_approved', 'mark_exclusive', 'unmark_exclusive']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    inlines = [BrandVendorInline]
    fieldsets = (
        ("Brand Name", {
            'fields': (
                'brand_name',
            ),
        }),
        ("Brand Other Setting", {
            'fields': (
                ('is_exclusive', 'is_recognised_brand', 'is_approved',)
            ),
        }),
    )
    list_display = (
        'brand_id', 'brand_name', 'image',
        'is_exclusive', 'is_recognised_brand', 'is_approved',
        'created_at', 'updated_at',
    )
    list_display_links = ('brand_id', 'image',)
    list_select_related = ('image',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('brand_id', 'brand_name',)
    autocomplete_fields = ('image',)
    ordering = ('-updated_at',)

    def mark_approved(self, request, queryset):
        queryset.update(is_approved=True)

    mark_approved.short_description = 'Mark Item Approved'

    def unmark_approved(self, request, queryset):
        queryset.update(is_approved=False)

    unmark_approved.short_description = 'Unmark Item Approved'

    def mark_exclusive(self, request, queryset):
        queryset.update(is_exclusive=True)

    mark_exclusive.short_description = 'Mark Item Exclusive'

    def unmark_exclusive(self, request, queryset):
        queryset.update(is_exclusive=False)

    unmark_exclusive.short_description = 'Unmark Item Exclusive'

    class Meta:
        model = Brand
