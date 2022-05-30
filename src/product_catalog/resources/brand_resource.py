from import_export import resources

from ..models import Brand


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        fields = ('brand_id', 'brand_name', 'image_id', 'is_recognised_brand', 'is_exclusive', 'is_approved')
        # exclude = ('brand_id',)
        import_id_fields = ('brand_id',)
