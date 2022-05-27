from django.db import models
from .image_mst import Image


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=255, null=False, blank=False, db_index=True, )
    region_description = models.TextField(null=True, blank=True)
    display_order = models.PositiveIntegerField(null=True, blank=True, db_index=True, )
    is_approved = models.BooleanField(default=False, db_index=True)
    image = models.OneToOneField(Image, null=True, blank=True, on_delete=models.CASCADE, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'regions'
        verbose_name = 'Region'

    def __str__(self):
        return f"{self.region_name}"
