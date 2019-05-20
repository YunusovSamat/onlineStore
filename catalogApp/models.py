from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcatalog(models.Model):
    fk_catalog = models.ForeignKey(
        Catalog, on_delete=models.SET_NULL, related_name='subcatalogs',
        null=True
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
