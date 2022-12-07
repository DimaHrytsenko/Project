from django.urls import path, include

from cart.views import AddProductToCartView, CartCreateView, CartView

app_name = 'cart'

urlpatterns = [
    # API pages
    path('api-add/', AddProductToCartView.as_view(), name='api-cart_products_add'),
    path('api-create/', CartCreateView.as_view(), name='api-cart_create'),
    path('api-view/', CartView.as_view(), name='api-cart_products_view'),
]
