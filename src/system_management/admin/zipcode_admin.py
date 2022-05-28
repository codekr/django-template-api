from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from djmoney.models.fields import MoneyField
from src.system_management.models import Zipcode


@admin.register(Zipcode)
class ZipcodeAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Forms", {
            # 'classes': ('wide',),
            'fields': (
                ('zipcode', 'zipcode_type'),
                'lat', 'long',
                ('city', 'state'),
                'country',
                'is_decommisioned'
            ),
        }),
    )

    list_display = ('zipcode', 'lat', 'long', 'city', 'state', 'country', 'created_at', 'updated_at')
    list_filter = ('city', 'state', 'updated_at')
    search_fields = ('city', 'state', 'zipcode', 'country')
    readonly_fields = ('country',)
    ordering = ('updated_at',)
