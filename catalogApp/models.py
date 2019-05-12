from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcatalog(models.Model):
    fk_catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, related_name='subcatalogs')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
