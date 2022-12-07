import rest_framework.request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse

from cart.models import Cart
from cart.serializers import AddToCartSerializer, CartSerializer
from product.models import Product



class CartCreateView(generics.CreateAPIView):
    queryset = Cart
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('customer:customer_login'))
        serializer.save(user=self.request.user)


class AddProductToCartView(generics.GenericAPIView):
    queryset = Cart
    serializer_class = AddToCartSerializer

    def post(self, request: rest_framework.request.Request, *args, **kwargs):
        user_cart: Cart = Cart.objects.filter(user=request.user.pk).first()
        if not user_cart:
            return Response({'detail': 'User has no cart'})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(Product, pk=serializer.data.get('product_pk'))
        user_cart.products.add(product)
        user_cart.save()
        return Response({'detail': 'Successfully added'})


class CartView(generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user_cart: Cart = Cart.objects.filter(user=request.user.pk).first()
        if not user_cart:
            return Response({'detail': 'User has no cart'})
        serializer = self.get_serializer(user_cart)
        return Response(serializer.data)
