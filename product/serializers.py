from rest_framework import serializers

from product.models import Product, Category, Payment, Delivery


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'image',
            'product_id',
            'name',
            'price',
        )


class ProductAddSerializer(serializers.ModelSerializer):
    in_stock = serializers.BooleanField(default=True)

    class Meta:
        model = Product
        fields = '__all__'


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category_id',
            'name',
        )


class RetrieveCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class GetPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'name',
            'url',
        )


class RetrievePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class GetDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = (
            'name',
        )


class RetrieveDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'