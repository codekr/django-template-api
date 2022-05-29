from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationChannelChoice(models.TextChoices):
    EMAIL = 'Email', _('EMAIL'),
    PUSH = 'Push', _('PUSH'),
    SMS = 'Sms', _('SMS'),


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification_name = models.CharField(
        max_length=255, db_index=True,
        verbose_name="Notification Name",
        help_text="Note: e.g Sales & Promotions or Personalized notifications"
    )
    notification_channel = models.CharField(
        max_length=30, db_index=True,
        choices=NotificationChannelChoice.choices,
        verbose_name="Notification Channel",
        help_text="Note: e.g Email, Sms, Push"
    )
    notification_additional_text = models.CharField(
        max_length=255,
        verbose_name="Notification Channel Description",
        help_text="Note: e.g Email Notification, Push Notification, Text Notification"
    )
    notification_description = models.TextField(
        max_length=255,
        verbose_name="Notification Description",
        help_text="Note: e.g Our top picks among new arrivals, best-sellers and limited-time deals."
    )
    is_allowed_to_disabled = models.BooleanField(
        default=False,
        verbose_name="Is User Allowed To Disabled?",
        help_text=""
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_mst'
        verbose_name = 'Notification'

    def __str__(self):
        return f"Notification: {self.notification_id}"
