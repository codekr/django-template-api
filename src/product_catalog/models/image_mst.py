from django.db import models


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=255, null=False, blank=False, db_index=True, )
    storage_id = models.CharField(max_length=255, null=True, blank=True, db_index=True, )
    alt_text = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    size = models.CharField(max_length=20, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'images'
        verbose_name = 'Image'

    def __str__(self):
        return f"{self.filename}"
