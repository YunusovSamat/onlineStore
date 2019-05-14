from django.db import models
from django.contrib.auth.models import User

from productApp.models import Product


# class Order(models.Model):
#     fk_client = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='order',
#         blank=True
#     )
#     date = models.DateField(auto_now_add=True)
#     finish = models.BooleanField(default=False)
#     sum = models.PositiveIntegerField(blank=True)
#
#
# class ProductOrder(models.Model):
#     fk_order = models.ForeignKey(
#         Order, on_delete=models.CASCADE, related_name='product_order'
#     )
#     fk_product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name='product_order'
#     )
#     count = models.PositiveIntegerField(default=1)
#     size = models.IntegerField()
