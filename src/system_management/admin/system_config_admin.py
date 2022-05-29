from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import SystemConfig


@admin.register(SystemConfig)
class SystemConfigAdmin(ImportExportModelAdmin):
    save_on_top = True
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '20', 'type': 'number'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ('Delivery Setting', {
            'fields': ('delivery_fee', 'add_tip_post_delivery_days', 'return_window_time'),
        }),
        ('Product Setting', {
            'classes': ('wide',),
            'fields': ('units_sold_threshold', 'quantity_remaining_threshold'),
        }),
        ('Product Tags Setting', {
            'classes': ('wide',),
            'fields': ('days_new_item', 'days_best_seller'),
        }),
        ('Product Review Setting', {
            'classes': ('wide',),
            'fields': ('is_show_review', 'max_orders_for_review', 'minimum_reviews_count'),
        }),
        ('Grocery Earn Points Setting', {
            'classes': ('wide',),
            'fields': ('points_expiry_days', 'points_dollar_conversion'),
        }),
        ('Referer Setting', {
            'classes': ('wide',),
            'fields': ('referer_sharing_cutoff_days', 'referee_purchase_cutoff_days', 'order_share_code_expiry')
        }),
        ('App Setting', {
            'classes': ('wide',),
            'fields': ('filter_sold_out_from_our_picks', 'mobile_app_landing_screen_seq', 'checkout_care_disclaimers'),
        }),
        ('Inventory Setting', {
            'classes': ('wide',),
            'fields': ('max_wholesale_threshold_to_sell',)
        }),
        ('Fulfillment Setting', {
            'classes': ('wide',),
            'fields': ('fulfillment_remaining_spot_threshold',)
        })
    )

    list_display = (
        'system_config_id', 'delivery_fee', 'add_tip_post_delivery_days', 'return_window_time', 'units_sold_threshold',
        'quantity_remaining_threshold', 'days_new_item', 'days_best_seller', 'is_show_review',
        # 'max_orders_for_review', 'minimum_reviews_count', 'points_expiry_days', 'points_dollar_conversion',
        # 'referer_sharing_cutoff_days', 'referee_purchase_cutoff_days', 'order_share_code_expiry',
        # 'referer_sharing_cutoff_days', 'referee_purchase_cutoff_days', 'order_share_code_expiry',
        # 'is_show_out_of_stock', 'mobile_app_landing_screen_seq', 'checkout_disclaimers',
        # 'max_wholesale_threshold_to_sell', 'fulfillment_remaining_spot_threshold'
    )
    ordering = ('-updated_at',)
