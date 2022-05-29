from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Item Name",
        help_text="Note: e.g 20 - 20 Nice"
    )
    item_alternate_name = models.TextField(
        max_length=255, null=True, blank=True, db_index=True,
        verbose_name="Item Alternate Name",
        help_text="Note: e.g Cookies, Biscuits, macaroons, Kukk_kal, Butter Cookies, Kukilu, Kukgalu, Bisketlu, "
                  "Nut Cookies "
    )
    is_approved = models.BooleanField(
        default=False, db_index=True,
        verbose_name="Is Approved?",
        help_text="Note: Mark the item as approved."
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'item_mst'
        verbose_name = 'Item'

    def __str__(self):
        return f"{self.item_name}({self.item_alternate_name})"
