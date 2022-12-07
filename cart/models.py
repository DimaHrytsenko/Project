from django.db import models

from product.models import Product
from customer.models import CustomUser


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, blank=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.user} trash bin'
