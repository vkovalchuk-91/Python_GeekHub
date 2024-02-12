import re

from rest_framework import serializers

from products.models import Product
from products.models import Category
from .tasks import run_scraping_task


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


class ProductIdsValidator:
    @staticmethod
    def validate_alpha_numeric_comma(value):
        pattern = re.compile("^[a-zA-Z0-9,]+$")
        if not pattern.match(value):
            raise serializers.ValidationError("Only Latin letters, numbers and commas are allowed.")
        return value


class AddProductsSerializer(serializers.Serializer):
    product_ids = serializers.CharField(validators=[ProductIdsValidator.validate_alpha_numeric_comma])

    def create(self, validated_data):
        print(validated_data["product_ids"])
        run_scraping_task.delay(ids=validated_data["product_ids"])
        return validated_data
