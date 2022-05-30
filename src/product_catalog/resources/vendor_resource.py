from import_export import resources

from ..models import Vendor


class VendorResource(resources.ModelResource):
    class Meta:
        model = Vendor
        fields = ('vendor_id', 'qb_id', 'company_name', 'address', 'address2', 'city', 'zip_pin_code',)
        # exclude = ('brand_id',)
        import_id_fields = ('vendor_id',)
