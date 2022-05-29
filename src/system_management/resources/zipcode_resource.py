from import_export import resources

from ..models import Zipcode


class ZipcodeResource(resources.ModelResource):
    class Meta:
        model = Zipcode
        fields = (
            'zipcode', 'city', 'state', 'lat', 'long', 'country', 'zipcode_type', 'is_decommisioned',)
