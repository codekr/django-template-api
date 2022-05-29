from colorfield.fields import ColorField
from django.db import models

from .image_mst import Image


class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255, null=False, blank=False, db_index=True,
        verbose_name="Sub Category Name",
        unique=True
    )
    description = models.TextField(
        max_length=300,
        null=True, blank=True,
        verbose_name="Description (optional)",
        help_text=""
    )
    display_order = models.PositiveSmallIntegerField(
        null=True, blank=True, db_index=True, default=1,
        verbose_name="Display Order",
        help_text="Note: Define the display order of the sub category for consumer application."
    )
    background_hex_code = ColorField(
        default=False, db_index=True,
        verbose_name="Background",
        help_text=""
    )
    is_approved = models.BooleanField(
        default=False, db_index=True,
        verbose_name="Is Approved?",
        help_text=""
    )
    is_tax_applicable = models.BooleanField(
        default=False, db_index=True,
        verbose_name="Is Tax Applicable?",
        help_text=""
    )
    effective_start_date = models.DateField(
        db_index=True, null=True, blank=True,
        verbose_name="Start Date",
        help_text="Note: This sub category will be only be shown starting this date."
    )
    effective_end_date = models.DateField(
        db_index=True, null=True, blank=True,
        verbose_name="End Date",
        help_text="Note: This sub category will not be shown after this date."
    )
    image = models.OneToOneField(Image, null=True, blank=True, on_delete=models.CASCADE, db_index=True, )
    categories = models.ManyToManyField(
        "Category", through="CategorySubCategory", db_index=True,
        verbose_name="Select category this belongs to?")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'sub_category_mst'
        verbose_name = 'Sub Category'
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return f"{self.name}"
