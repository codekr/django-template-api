from django.db import models
from djmoney.models.fields import MoneyField


class SystemConfig(models.Model):
    """
        Define the System configuration schema
    """
    system_config_id = models.AutoField(primary_key=True)
    delivery_fee = MoneyField(
        null=True,
        blank=False, max_digits=3, decimal_places=2, default_currency='USD',
        verbose_name='Delivery Fee')

    points_expiry_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Point expires in day',
        verbose_name='Earn Point Expire')

    days_new_item = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Show 'new tag', if the product added in the following day"
    )
    days_best_seller = models.PositiveIntegerField(null=True, blank=True)
    add_tip_post_delivery_days = models.PositiveIntegerField(null=True, blank=True)
    is_show_review = models.BooleanField(default=False)
    minimum_reviews_count = models.PositiveIntegerField(null=True, blank=True)
    units_sold_threshold = models.PositiveIntegerField(null=True, blank=True)
    quantity_remaining_threshold = models.PositiveIntegerField(null=True, blank=True)
    points_dollar_conversion = models.PositiveIntegerField(null=True, blank=True)
    referer_sharing_cutoff_days = models.PositiveIntegerField(null=True, blank=True)
    referee_purchase_cutoff_days = models.PositiveIntegerField(null=True, blank=True)
    return_window_time = models.PositiveIntegerField(null=True, blank=True)
    max_wholesale_threshold_to_sell = models.PositiveIntegerField(null=True, blank=True)
    order_share_code_expiry = models.PositiveIntegerField(null=True, blank=True)
    max_orders_for_review = models.PositiveIntegerField(null=True, blank=True)
    mobile_app_landing_screen_seq = models.CharField(max_length=128, null=True, blank=True)
    checkout_care_disclaimers = models.TextField(null=True, blank=True)
    filter_sold_out_from_our_picks = models.BooleanField(default=False)
    fulfillment_remaining_spot_threshold = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'system_config'
        verbose_name = 'SystemConfig'

    def __str__(self):
        return f"{self.system_config_id}"
