import django.core.handlers.wsgi
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import generics, serializers
from rest_framework.generics import get_object_or_404
from django.http import HttpResponseRedirect
from product.forms import ReviewForm
from product.models import Product, Category, Payment, Delivery
from product.paginators import CustomPagination
from product.serializers import ProductSerializers, ProductAddSerializer, GetCategorySerializer, GetPaymentSerializer, \
    GetDeliverySerializer, RetrieveCategorySerializer, RetrievePaymentSerializer, RetrieveDeliverySerializer


class HomepageView(TemplateView):
    template_name = 'shop/homepage.html'
    extra_context = {
        'categories': Category.objects.all()
    }


class MonoPaymentView(TemplateView):
    template_name = 'payments/Mono.html'


class Privat24PaymentView(TemplateView):
    template_name = 'payments/Privat24.html'


class GetCandlesView(TemplateView):
    template_name = 'shop/candles/candles_catalog.html'

    def get(self, request, *args, **kwargs):
        filter_ = request.GET.get('filter')
        context = dict()
        if filter_ == 'A-Z':
            context['candles'] = Product.objects.all().filter(category_id='С0001').order_by('name')
        elif filter_ == 'Z-A':
            context['candles'] = Product.objects.all().filter(category_id='С0001').order_by('-name')
        else:
            context['candles'] = Product.objects.filter(category_id='С0001').all()
        print(context)
        return self.render_to_response(context)


class GetDiffusersView(TemplateView):
    template_name = 'shop/diffuser/diffuser_catalog.html'

    def get(self, request, *args, **kwargs):
        filter_ = request.GET.get('filter')
        context = dict()
        if filter_ == 'A-Z':
            context['diffusers'] = Product.objects.all().filter(category_id='C0002').order_by('name')
        elif filter_ == 'Z-A':
            context['diffusers'] = Product.objects.all().filter(category_id='C0002').order_by('-name')
        else:
            context['diffusers'] = Product.objects.filter(category_id='C0002').all()
        print(context)
        return self.render_to_response(context)


class DetailView(TemplateView):
    template_name = 'shop/detail_page.html'

    def get(self, request: django.core.handlers.wsgi.WSGIRequest, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        self.extra_context = {'product': product}
        return self.render_to_response(self.get_context_data(**kwargs))


class ReviewView(TemplateView):
    template_name = 'shop/review.html'

    def get(self, request: django.core.handlers.wsgi.WSGIRequest, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('customer:customer_login'))
        product = get_object_or_404(Product, pk=pk)
        self.extra_context = {'form': ReviewForm(data={'product': product.pk, 'user': request.user.pk})}
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request: django.core.handlers.wsgi.WSGIRequest, *args, **kwargs):
        data = request.POST
        ReviewForm(data).save()
        return HttpResponseRedirect(reverse('product:product_detail', kwargs={'pk': data.get('product')}))


class GetProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('product_id')
    serializer_class = ProductSerializers
    pagination_class = CustomPagination


class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAddSerializer


class AddProductView(generics.CreateAPIView):
    in_stock = serializers.BooleanField(default=True)
    queryset = Product.objects.all()
    serializer_class = ProductAddSerializer
    # permission_classes = (IsAdminUser,)


class GetCategoryView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('category_id')
    serializer_class = GetCategorySerializer
    pagination_class = CustomPagination
    # permission_classes = (IsAdminUser,)


class RetrieveUpdateDestroyCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('category_id')
    serializer_class = RetrieveCategorySerializer
    pagination_class = CustomPagination
    # permission_classes = (IsAdminUser,)


class GetPaymentView(generics.ListAPIView):
    queryset = Payment.objects.all().order_by('name')
    serializer_class = GetPaymentSerializer
    pagination_class = CustomPagination
    # permission_classes = (IsAdminUser,)


class RetrieveUpdateDestroyPaymentView(generics.ListAPIView):
    queryset = Payment.objects.all().order_by('name')
    serializer_class = RetrievePaymentSerializer
    pagination_class = CustomPagination
    # permission_classes = (IsAdminUser,)


class GetDeliveryView(generics.ListAPIView):
    queryset = Delivery.objects.all().order_by('name')
    serializer_class = GetDeliverySerializer
    pagination_class = CustomPagination
    # permission_classes = (IsAdminUser,)


class RetrieveUpdateDestroyDeliveryView(generics.ListAPIView):
    queryset = Delivery.objects.all().order_by('name')
    serializer_class = RetrieveDeliverySerializer
    pagination_class = CustomPagination
    # permission_classes = (IsAdminUser,)
