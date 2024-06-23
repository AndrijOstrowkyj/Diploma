from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    description = models.CharField(max_length = 200)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.name


class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviews_txt = models.CharField(max_length = 100)

    def __str__(self):
        return self.reviews_txt


class Order(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="99")
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    post_type = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=100, default="")
    postal_code = models.CharField(max_length=20, default="")
    payment_type = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"Order #{self.pk} - Total: {self.total_price} $"
    