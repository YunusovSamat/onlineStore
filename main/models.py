from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcatalog(models.Model):
    catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, related_name='catalog')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    subcatalog = models.ForeignKey(
        Subcatalog, on_delete=models.CASCADE, related_name='subcatalog')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class ImageProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=100)
    image = models.ImageField(
        blank=True, upload_to='static/main/imagesProduct')

    def __str__(self):
        return self.name


class ImagePage(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='static/main/imagesPage')

    def __str__(self):
        return self.slug
