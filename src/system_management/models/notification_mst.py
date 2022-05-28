from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationTypeChoice(models.TextChoices):
    Email = 'Email', _('Email'),
    Push = 'Push', _('Push'),
    Text = 'Text', _('Text'),


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification_name = models.CharField(max_length=255, null=False, blank=False, db_index=True)
    notification_type = models.CharField(
        max_length=120, db_index=True, null=False, blank=False,
        choices=NotificationTypeChoice.choices)
    notification_description = models.TextField(null=False, blank=False)
    notification_type_additional_text = models.TextField(null=False, blank=False)
    is_allowed_to_disabled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_mst'
        verbose_name = 'Notification'

    def __str__(self):
        return f"Notification: {self.notification_id}"
