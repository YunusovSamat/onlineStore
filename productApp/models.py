from django.db import models

from catalogApp .models import Subcatalog


class Product(models.Model):
    fk_subcatalog = models.ForeignKey(
        Subcatalog, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    old_price = models.PositiveIntegerField(default=0, blank=True)
    new = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class SizeProduct(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return str(self.size)


class CountProduct(models.Model):
    fk_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='counts')
    fk_size = models.ForeignKey(
        SizeProduct, on_delete=models.CASCADE, related_name='counts')
    count = models.PositiveIntegerField(default=100)

    def __str__(self):
        return str(self.count)

    class Meta:
        ordering = ['fk_size']


class ImageProduct(models.Model):
    fk_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images_product')
    image = models.ImageField(
        blank=True, upload_to='imagesProduct')

    def __str__(self):
        return str(self.image)
