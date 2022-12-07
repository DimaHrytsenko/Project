from django.db import models

from customer.models import CustomUser


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    category_id = models.CharField(max_length=5,
                                   primary_key=True)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class Delivery(models.Model):
    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'

    name = models.CharField(max_length=128,
                            primary_key=True)
    image = models.ImageField(upload_to='delivery/')

    def __str__(self):
        return self.name


class Review(models.Model):
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    MARKS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(CustomUser, models.CASCADE)
    text = models.TextField(max_length=1024)
    mark = models.IntegerField(choices=MARKS)
    product = models.ForeignKey('Product', models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.mark}'


class Payment(models.Model):
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'payments'

    name = models.CharField(max_length=128,
                            primary_key=True)
    url = models.URLField(null=True,
                          blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    product_id = models.CharField(max_length=5,
                                  primary_key=True)
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    in_stock = models.BooleanField(blank=True,
                                   default=True)
    description = models.TextField(max_length=1024,
                                   null=True,
                                   blank=True)
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_id} {self.name}'
