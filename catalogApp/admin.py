from django.contrib import admin

from .models import Catalog, Subcatalog
from productApp.models import Product


class SubcatalogInline(admin.TabularInline):
    model = Subcatalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name', 'id']
    ordering = ['name', 'id']
    inlines = [SubcatalogInline]


class ProductInline(admin.TabularInline):
    model = Product


class SubcatalogAdmin(admin.ModelAdmin):
    list_display = ['fk_catalog', 'name', 'id']
    search_fields = ['fk_catalog', 'name', 'id']
    ordering = ['fk_catalog', 'name', 'id']
    inlines = [ProductInline]


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Subcatalog, SubcatalogAdmin)

