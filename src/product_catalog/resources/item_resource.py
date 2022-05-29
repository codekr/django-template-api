from import_export import resources

from ..models import Item


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        fields = ('item_id', 'item_name', 'item_alternate_name', 'is_approved')
        import_id_fields = ('item_id',)
