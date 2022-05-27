from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255, null=False, blank=False, db_index=True, )
    item_alternate_name = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    is_approved = models.BooleanField(default=False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'

    def __str__(self):
        return f"{self.item_name}({self.item_alternate_name})"
