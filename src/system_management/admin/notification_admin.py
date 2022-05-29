from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Notification


@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin):
    required_css_class = 'required'
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Mandatory Fields", {
            'fields': (
                'notification_name', 'notification_channel',
                ('notification_description', 'notification_additional_text',),
                'is_allowed_to_disabled',
            ),
        }),
    )

    list_display = (
        'notification_id', 'notification_name', 'notification_channel', 'is_allowed_to_disabled', 'created_at',
        'updated_at',
    )
    list_filter = ('notification_channel',)
    search_fields = ('notification_id', 'notification_name', 'notification_channel')
    ordering = ('updated_at',)
