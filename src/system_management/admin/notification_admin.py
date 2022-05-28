from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from djmoney.models.fields import MoneyField
from src.system_management.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }
    fieldsets = (
        (None, {
            'fields': (
                ('notification_name', 'notification_type',),
                'notification_description',
                'notification_type_additional_text',
                'is_allowed_to_disabled',
            ),
        }),
    )

    list_display = (
        'notification_id', 'notification_name', 'notification_type', 'is_allowed_to_disabled', 'created_at',
        'updated_at',
    )
    list_filter = ('notification_type',)
    search_fields = ('notification_id', 'notification_name', 'notification_type')
    ordering = ('updated_at',)
