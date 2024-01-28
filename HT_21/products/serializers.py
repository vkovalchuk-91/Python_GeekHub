from rest_framework import serializers

from products.models import Product
from products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'product_id',
            'name',
            'price',
            'short_description',
            'brand',
            'category',
            'link_to_product',
            'update_date'
        ]
