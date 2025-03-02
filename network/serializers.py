from rest_framework import serializers

from network.models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=NetworkNode.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'model', 'release_date', 'supplier')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = ('id', 'name', 'country', 'city')


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    supplier = SupplierSerializer(read_only=True)
    level = serializers.SerializerMethodField()
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

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
            'products',
            'level'
        )

    def get_level(self, obj):
        return obj.get_level()
