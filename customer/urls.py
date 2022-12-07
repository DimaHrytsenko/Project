from django.urls import path

from customer.views import CustomLoginView, CustomLogoutView

app_name = 'customer'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='customer_login'),
    path('logout/', CustomLogoutView.as_view(), name='customer_logout'),
]
