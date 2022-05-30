from import_export import resources

from ..models import SubCategory


class SubCategoryResource(resources.ModelResource):
    class Meta:
        model = SubCategory
        fields = (
            'sub_category_id', 'name', 'category', 'description', 'display_order', 'image_id',
            'is_approved', 'is_tax_applicable', 'effective_start_date', 'effective_end_date', 'background_hex_code'
        )
        import_id_fields = ('sub_category_id',)
