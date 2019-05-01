from django.db import models


# class Order(models.Model):
#     fk_client = models.ForeignKey(
#         Client, on_delete=models.CASCADE, related_name='order')
#     date = models.DateField(auto_now_add=True)
#     finish = models.
#     sum = models.PositiveIntegerField(blank=True)
#
#
# class ProductOrder(models.Model):
#     fk_order = models.ForeignKey(
#         Order, on_delete=models.CASCADE, related_name='product_order')
#     count = models.PositiveIntegerField(default=1)
#     size = models.IntegerField()
