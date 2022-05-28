from django.db import models
from django.utils.translation import gettext_lazy as _


class ReasonTypeChoice(models.TextChoices):
    Product = 'Product', _('Product'),
    Delivery_Pickup = 'Delivery_Pickup', _('Delivery/Pickup'),


class Reason(models.Model):
    reason_id = models.AutoField(primary_key=True)
    reason_label = models.TextField(
        max_length=255, null=False, blank=False, db_index=True,
        verbose_name="Reason Label",
        help_text="e.g Ordering experience, Technology related"
    )
    reason_type = models.CharField(
        max_length=120, db_index=True, null=False, blank=False,
        choices=ReasonTypeChoice.choices,
        verbose_name="Reason Type",
        help_text="e.g Delivery/Pickup, Product"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reason_mst'
        verbose_name = 'Reason Option'

    def __str__(self):
        return f"Issue Reason: {self.issue_reason_id}"
