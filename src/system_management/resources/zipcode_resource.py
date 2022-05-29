from import_export import resources

from ..models import Zipcode


class ZipcodeResource(resources.ModelResource):
    class Meta:
        model = Zipcode
        fields = (
            'zipcode', 'name', 'state', 'county', 'lat', 'long', 'country', 'type', 'is_decommisioned')
        import_id_fields = ('zipcode',)
