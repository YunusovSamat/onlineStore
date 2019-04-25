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
