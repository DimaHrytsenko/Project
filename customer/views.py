import rest_framework.request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.views import APIView

from customer.models import CustomUser


class CustomLoginView(TemplateView, APIView):
    template_name = 'customer/login.html'

    def post(self, request: rest_framework.request.Request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            CustomUser(email=email, password=make_password(password)).save()
            return self.render_to_response({'user_created': 'User has been created successfully'})
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('product:homepage'))


class CustomLogoutView(APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('customer:customer_login'))
