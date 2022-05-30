from import_export import resources

from ..models import Category


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = (
            'category_id', 'name', 'description', 'display_order', 'image_id', 'background_hex_code', 'is_approved')
        # exclude = ('brand_id',)
        import_id_fields = ('category_id',)
