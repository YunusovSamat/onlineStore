from django.db import models
from django.contrib.auth.models import User

from productApp.models import Product


class Order(models.Model):
    fk_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=150, blank=True)
    surname = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    date = models.DateField(auto_now_add=True)
    address = models.TextField()
    comment = models.TextField(blank=True)
    delivery_price = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)


class ProductOrder(models.Model):
    fk_order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='product_order'
    )
    fk_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_order'
    )
    count = models.PositiveIntegerField(default=1)
    size = models.IntegerField()

    def __str__(self):
        return str(self.fk_product)
