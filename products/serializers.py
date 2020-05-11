from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'img_path',
            'quantity',
            'price',
            'text',
            'condition_code',
            'insert_date',
            'update_date',
            'published_date'
            )