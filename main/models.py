from django.db import models


class Catalog(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.slug


class Subcatalog(models.Model):
    fk_catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, related_name='catalog')
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.slug


class Product(models.Model):
    fk_subcatalog = models.ForeignKey(
        Subcatalog, on_delete=models.CASCADE, related_name='subcatalog')
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.slug


class SizeProduct(models.Model):
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size


class CountProduct(models.Model):
    fk_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='fk_product')
    fk_size = models.ForeignKey(
        SizeProduct, on_delete=models.CASCADE, related_name='fk_size')
    count = models.PositiveIntegerField(default=100)

    def __str__(self):
        return str(self.count)


class ImageProduct(models.Model):
    fk_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product')
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        blank=True, upload_to='static/main/imagesProduct')

    def __str__(self):
        return self.slug


class ImagePage(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField(blank=True, upload_to='static/main/imagesPage')

    def __str__(self):
        return self.slug
