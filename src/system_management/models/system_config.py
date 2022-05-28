from django.db import models
from djmoney.models.fields import MoneyField


class SystemConfig(models.Model):
    """
        Define the System configuration schema
    """
    system_config_id = models.AutoField(primary_key=True)
    delivery_fee = MoneyField(
        null=True,
        blank=False, max_digits=4, decimal_places=2, default_currency='USD',
        verbose_name='Delivery Fee',
        help_text="Delivery fee if minimum order amount is not met."
    )
    points_expiry_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Points Expiry Days',
        help_text='Number of days after which the points will expire. 0 means points will never expire.',
    )
    days_new_item = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Days New Item',
        help_text="This will be used to add the 'new' tag to the product. Example if this as a value of 7 means any "
                  "new products added in the last 7 days will get the 'new tag'. "
    )
    days_best_seller = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Days Best Seller',
        help_text="This will be used to auto select products based on units sold of products in last X days. For "
                  "example: if this field as a value of 7, then show those products which have sold the most in the "
                  "last 7 days. "
    )
    add_tip_post_delivery_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Add Tip Post Delivery Days',
        help_text="This config will be used to control how many days after delivery the customer can increase tip. "
                  "For example if the value is 7, then the option to increase tip or add tip post delivery should be "
                  "available for 7 days. "
    )
    is_show_review = models.BooleanField(
        default=False,
        verbose_name='Is Show Review?',
        help_text="Configure to show system wide reviews in the user facing application."
    )
    minimum_reviews_count = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Minimum Review Count",
        help_text="Number of reviews before they show up on the app to customers."
    )
    units_sold_threshold = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Units Sold Threshold",
        help_text="This controls the minimum no. of units sold before showing the label '3k+ sold' on the app."
    )
    quantity_remaining_threshold = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Quantity Remaining Threshold",
        help_text="Show quantities remaining if the remaining quantities is less than X units."
    )
    points_dollar_conversion = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Points Dollar Conversion",
        help_text="X points earned on each dollar for order placed. Ex: X = 1, all customers including super members "
                  "will earn 1 points for each dollar for order placed. "
    )
    referer_sharing_cutoff_days = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Referer Sharing Cutoff Days.",
        help_text="After order is delivered or picked up."
    )
    referee_purchase_cutoff_days = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Referee Purchase Cutoff Days",
        help_text="Referee should make the purchase within X days or clicking on the link."
    )
    return_window_time = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Return Window Time",
        help_text="System wide return window after which the returns won't be allowed."
    )
    max_wholesale_threshold_to_sell = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Max Wholesale Threshold To Sell",
        help_text="This value will be in percentage. This is the setting to calculate the max inventory from "
                  "wholesale. Example take 90% wholesale_quantity and add it to to the 100% retail_quantity. "
    )
    order_share_code_expiry = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Order Share Code Expiry",
        help_text="Time after which the order share code will be expired."
    )
    max_orders_for_review = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Max Orders For Review",
        help_text="This will be used on the 'my reviews' screen in my account to show hte no. of orders for review."
    )
    mobile_app_landing_screen_seq = models.CharField(
        max_length=30,
        null=True, blank=True, verbose_name="Mobile App Landing Screen Sequence",
        help_text="Screen names: login, signup This will be used to decide which screen will the user see when "
                  "he/she/other open the app the first time. "
    )
    checkout_care_disclaimers = models.TextField(
        null=True, blank=True, verbose_name="Checkout Care Disclaimer",
        help_text="Provide the instruction to user on checkout screen."
    )
    filter_sold_out_from_our_picks = models.BooleanField(
        default=False,
        verbose_name="Is Filter Sold Out From Our Picks?",
        help_text="'Check' means filter out all out of stock items,  'Uncheck' means show all out of stock of item in "
                  "put picks. "
    )
    fulfillment_remaining_spot_threshold = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Fulfillment Remaining Spot Threshold",
        help_text="Number of reviews before they show up on the app to customers."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'system_config_mst'
        verbose_name = 'System Configuration'

    def __str__(self):
        return f"{self.system_config_id}"
