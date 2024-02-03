from rest_framework import serializers

from products.models import Product
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()


class CartSerializer(serializers.Serializer):
    cart_items = serializers.ListField(child=CartItemSerializer())


class CartAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    @staticmethod
    def validate_product_id(value):
        try:
            Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product with this id does not exist.")
        return value


class CartUpdateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    @staticmethod
    def validate_product_id(value):
        try:
            Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product with this id does not exist.")
        return value

    @staticmethod
    def validate_quantity(value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")
        return value


class CartDeleteSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=False)

    @staticmethod
    def validate_product_id(value):
        try:
            Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product with this id does not exist.")
        return value
