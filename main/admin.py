from django.contrib import admin

from .models import Catalog, Subcatalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    search_fields = ['slug', 'name']
    ordering = ['slug']


class SubcatalogAdmin(admin.ModelAdmin):
    list_display = ['fk_catalog', 'slug', 'name']
    search_fields = ['fk_catalog', 'slug', 'name']
    ordering = ['fk_catalog', 'slug']


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Subcatalog, SubcatalogAdmin)

