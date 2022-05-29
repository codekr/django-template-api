from colorfield.fields import ColorField
from django.db import models

from .image_mst import Image


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255, null=False, blank=False, db_index=True, verbose_name="Category Name",
        unique=True
    )
    description = models.TextField(
        max_length=300,
        null=True, blank=True,
        verbose_name="Description",
        help_text="Note: e.g describe the about the category."
    )
    display_order = models.PositiveSmallIntegerField(
        null=True, blank=True, db_index=True, default=1,
        verbose_name="Display Order",
        help_text="Note: Define the display order of the category to consumer application."
    )
    background_hex_code = ColorField(
        default=False, db_index=True,
        verbose_name="Background Color",
        help_text=""
    )
    is_approved = models.BooleanField(
        default=False, db_index=True,
        verbose_name="Is Approved ?",
        help_text="Note: Mark the category as approved."
    )
    image = models.OneToOneField(Image, null=True, blank=True, on_delete=models.CASCADE, db_index=True, )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'category_mst'
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"
