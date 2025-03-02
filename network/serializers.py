from rest_framework import serializers

from network.models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=NetworkNode.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'model', 'release_date', 'supplier')


class SupplierSerializer(serializers.ModelSerializer):
    level_display = serializers.SerializerMethodField()

    class Meta:
        model = NetworkNode
        fields = ('id', 'name', 'country', 'city', 'level_display')

    def get_level_display(self, obj):
        """ Returns textual representation of the level """
        return obj.level_display


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=NetworkNode.objects.all(), allow_null=True, write_only=True)
    supplier_details = SupplierSerializer(source='supplier', read_only=True)
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    level_display = serializers.SerializerMethodField()

    class Meta:
        model = NetworkNode
        fields = (
            'id',
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'debt',
            'created_at',
            'supplier',
            'supplier_details',
            'products',
            'level_display'
        )

    def get_level_display(self, obj):
        """ Returns textual representation of the level """
        return obj.level_display
