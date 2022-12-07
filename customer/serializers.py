from rest_framework import serializers

from customer.models import CustomUser


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
