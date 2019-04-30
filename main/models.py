from django.db import models


class Catalog(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.slug


class Subcatalog(models.Model):
    fk_catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, related_name='subcatalogs')
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.slug


# class Order(models.Model):
#     fk_client = models.ForeignKey(
#         Client, on_delete=models.CASCADE, related_name='order')
#     date = models.DateField(auto_now_add=True)
#     finish = models.
    # sum = models.PositiveIntegerField(blank=True)
#
#
# class ProductOrder(models.Model):
#     fk_order = models.ForeignKey(
#         Order, on_delete=models.CASCADE, related_name='product_order')
#     count = models.PositiveIntegerField()
#     fk_size = models.ForeignKey(
#         SizeProduct, on_delete=models.CASCADE, related_name='product_order')
