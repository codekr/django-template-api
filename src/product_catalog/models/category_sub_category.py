from django.db import models

from .category_mst import Category
from .sub_category_mst import SubCategory


class CategorySubCategory(models.Model):
    category_sub_category_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_index=True,
        verbose_name="Category Name",
        help_text=""
    )
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, db_index=True,
        verbose_name="Sub Category Name",
        help_text=""
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'category_sub_category_link'
        verbose_name = ''
        unique_together = ('category_sub_category_id', 'category', 'sub_category',)

    def __str__(self):
        return "{}_{}".format(self.category.__str__(), self.sub_category.__str__())
