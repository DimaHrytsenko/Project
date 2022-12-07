from django.contrib import admin

from product.models import Delivery, Review, Payment, Product, Category

admin.site.register(Delivery)
admin.site.register(Review)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Category)
