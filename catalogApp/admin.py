from django.contrib import admin

from .models import Catalog, Subcatalog
from productApp.models import Product


class SubcatalogInline(admin.TabularInline):
    model = Subcatalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    ordering = ['id', 'name']
    inlines = [SubcatalogInline]


class ProductInline(admin.TabularInline):
    model = Product


class SubcatalogAdmin(admin.ModelAdmin):
    list_display = ['fk_catalog', 'name', 'id']
    ordering = ['fk_catalog', 'id', 'name']
    inlines = [ProductInline]


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Subcatalog, SubcatalogAdmin)

