from rest_framework import serializers

from cart.models import Cart
from product.serializers import ProductAddSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ProductAddSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class AddToCartSerializer(serializers.Serializer):
    product_pk = serializers.CharField()
