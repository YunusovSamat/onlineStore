from django.contrib import admin

from .models import Catalog, Subcatalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['id']


class SubcatalogAdmin(admin.ModelAdmin):
    list_display = ['fk_catalog', 'id', 'name']
    search_fields = ['fk_catalog', 'id', 'name']
    ordering = ['fk_catalog', 'id']


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Subcatalog, SubcatalogAdmin)

