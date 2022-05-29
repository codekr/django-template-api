from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Tax
from ..resources import TaxResource


@admin.register(Tax)
class TaxAdmin(ImportExportModelAdmin):
    resource_class = TaxResource
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Zipcode Information", {
            'fields': (
                'zipcode',
            ),
        }),
        ("Tax", {
            'fields': (
                ('state_rate', 'county_rate', 'city_rate', 'special_rate',),
                'combined_district_rate',
            ),
        }),
        ("Other Information", {
            'fields': (
                'status',
                'is_freight_taxable'
            ),
        }),
    )

    list_display = (
        'tax_rate_id', 'zipcode', 'state_rate', 'special_rate', 'city_rate', 'county_rate', 'combined_district_rate',
        'is_freight_taxable', 'created_at',
    )
    list_select_related = ('zipcode',)
    list_filter = ('updated_at', 'is_freight_taxable',)
    autocomplete_fields = ('zipcode',)
    search_fields = ('tax_rate_id', 'state_rate', 'county_rate', 'city_rate', 'combined_district_rate', 'special_rate')
    ordering = ('updated_at',)
    list_per_page = 150
