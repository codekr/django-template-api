from import_export import resources

from ..models import Tax


class TaxResource(resources.ModelResource):
    class Meta:
        model = Tax
        fields = (
            'tax_rate_id', 'zipcode', 'state_rate', 'county_rate', 'city_rate', 'combined_district_rate',
            'is_freight_taxable',
            'special_rate')
        import_id_fields = ('tax_rate_id',)
