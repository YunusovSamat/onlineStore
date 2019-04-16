from django.db import models


class Catalog(models.Model):
    catalog_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catalog_name


class Subcatalog(models.Model):
    subcatalog_name = models.CharField(max_length=100)
    # set name
    subcatalog_catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcatalog_name


class Product(models.Model):
    # set name
    product_subcatalog = models.ForeignKey(Subcatalog,
                                           on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.PositiveIntegerField(default=0)
    product_count = models.PositiveIntegerField(default=100)
    product_description = models.TextField(blank=True)

    def __str__(self):
        return self.product_name


class ImageProduct(models.Model):
    image_product_name = models.CharField(max_length=100)
    image_product_image = models.ImageField(blank=True,
                                            upload_to='static/main/images')
    # set name
    image_product_product = models.ForeignKey(Product,
                                              on_delete=models.CASCADE)

    def __str__(self):
        return self.image_product_name
