from django.contrib import admin

# Register your models here.

from .models import Product, Reviews, Order

admin.site.register(Product)
admin.site.register(Reviews)
admin.site.register(Order)