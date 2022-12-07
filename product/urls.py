from django.urls import path

from product.views import HomepageView, GetProductListView, Privat24PaymentView, MonoPaymentView, AddProductView, \
    GetCategoryView, GetPaymentView, GetDeliveryView, RetrieveUpdateDestroyProductView, \
    RetrieveUpdateDestroyCategoryView, RetrieveUpdateDestroyPaymentView, RetrieveUpdateDestroyDeliveryView, \
    GetCandlesView, GetDiffusersView, DetailView, ReviewView

app_name = 'product'

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('candles/', GetCandlesView.as_view(), name='candles'),
    path('diffusers/', GetDiffusersView.as_view(), name='diffusers'),
    path('detail/<pk>', DetailView.as_view(), name='product_detail'),
    path('review/<pk>', ReviewView.as_view(), name='product_review'),

    # API pages
    path('api-products/', GetProductListView.as_view(), name='api-products'),
    path('api-product/details/<pk>/', RetrieveUpdateDestroyProductView.as_view(), name='api-product_details'),
    path('api-add_product/', AddProductView.as_view(), name='api-add_product'),
    path('api-get_category/', GetCategoryView.as_view(), name='api-get_category'),
    path('api-category/details/<pk>', RetrieveUpdateDestroyCategoryView.as_view(), name='api-retrieve_category'),
    path('api-get_payment/', GetPaymentView.as_view(), name='api-get_payment'),
    path('api-category/details/<pk>', RetrieveUpdateDestroyPaymentView.as_view(), name='api-retrieve_payment'),
    path('api-get_delivery/', GetDeliveryView.as_view(), name='api-get_delivery'),
    path('api-category/details/<pk>', RetrieveUpdateDestroyDeliveryView.as_view(), name='api-retrieve_delivery'),
    path('Privat24/', Privat24PaymentView.as_view(), name='Privat24'),
    path('Mono/', MonoPaymentView.as_view(), name='Mono'),
]
