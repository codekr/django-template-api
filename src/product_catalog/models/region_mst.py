from django.db import models

from .image_mst import Image


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255, db_index=True, unique=True,
        verbose_name="Name",
        help_text="Note: e.g Bengali, Gujarati, Kashmiri, Luchnowi, Maharashtrian."
    )
    description = models.TextField(
        max_length=300,
        null=True, blank=True,
        verbose_name="Description",
        help_text="Note: e.g describe the about the region."
    )
    display_order = models.PositiveSmallIntegerField(
        null=True, blank=True, db_index=True, default=1,
        verbose_name="Display Order",
        help_text="Note: Define the display order of region in consumer phasing application."
    )
    is_approved = models.BooleanField(
        default=False, db_index=True,
        verbose_name="Is Approved?",
        help_text="Note: Mark the Region as approved."
    )
    image = models.OneToOneField(Image, null=True, blank=True, on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'region_mst'
        verbose_name = 'Region'

    def __str__(self):
        return f"{self.name}"
