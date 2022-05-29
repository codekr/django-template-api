from django.db import models


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    filename = models.CharField(
        max_length=255, db_index=True,
        verbose_name="Filename",
    )
    storage_id = models.CharField(
        max_length=255, null=True, blank=True, db_index=True,
        verbose_name="Storage Bucket Key",
    )
    alt_text = models.CharField(
        max_length=255, null=True, blank=True,
        verbose_name="Alternate Text",
        help_text=""
    )
    type = models.CharField(
        max_length=20, null=True, blank=True,
        verbose_name="Type",
        help_text=""
    )
    size = models.CharField(
        max_length=20, null=True, blank=True,
        verbose_name="Size",
        help_text=""
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'image_mst'
        verbose_name = 'Image'

    def __str__(self):
        return f"{self.filename}"
