from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Zipcode
from ..resources import ZipcodeResource


@admin.register(Zipcode)
class ZipcodeAdmin(ImportExportModelAdmin):
    resource_class = ZipcodeResource
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Forms", {
            'fields': (
                ('zipcode', 'type'),
                'lat', 'long',
                ('name', 'state', 'county'),
                'country',
                'is_decommisioned'
            ),
        }),
    )

    list_display = ('zipcode', 'name', 'state', 'county', 'lat', 'long', 'country', 'created_at', 'updated_at')
    list_filter = ('state', 'updated_at')
    search_fields = ('name', 'state', 'zipcode', 'country', 'county')
    readonly_fields = ('country',)
    ordering = ('-updated_at',)
    list_per_page = 150
