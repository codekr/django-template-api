from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from djmoney.models.fields import MoneyField
from src.system_management.models import Tax


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }
    fieldsets = (
        (None, {
            'fields': (
                'zipcode',
                ('state_rate', 'county_rate', 'special_rate',),
                'combined_district_rate',
                'is_freight_taxable',
                'status',
            ),
        }),
    )

    list_display = (
        'tax_rate_id', 'zipcode', 'state_rate', 'special_rate', 'county_rate', 'combined_district_rate',
        'is_freight_taxable', 'created_at', 'updated_at',
    )
    list_select_related = ('zipcode',)
    list_filter = ('is_freight_taxable',)
    autocomplete_fields = ('zipcode',)
    search_fields = ('tax_rate_id', 'state_rate', 'county_rate', 'combined_district_rate', 'special_rate')
    ordering = ('updated_at',)
