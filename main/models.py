from django.db import models


class Catalog(models.Model):
    catalog_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catalog_name


class Subcatalog(models.Model):
    subcatalog_name = models.CharField(max_length=100)
    subcatalog_catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcatalog_name


class Product(models.Model):
    product_subcatalog = models.ForeignKey(Subcatalog, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.PositiveIntegerField(default=0)
    product_count = models.PositiveIntegerField(default=100)
    product_description = models.TextField(default='')
    product_image = models.ImageField(default=0)

    def __str__(self):
        return self.product_name

