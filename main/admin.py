from django.contrib import admin

from .models import Catalog, Subcatalog, Product


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['catalog_name']
    search_fields = ['catalog_name']


admin.site.register(Catalog, CatalogAdmin)


class SubcatalogAdmin(admin.ModelAdmin):
    list_display = ['subcatalog_name', 'subcatalog_catalog']
    search_fields = ['subcatalog_name']


admin.site.register(Subcatalog, SubcatalogAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_subcatalog', 'product_name', 'product_price',
        'product_count', 'product_description', 'product_image'
    ]
    search_fields = ['product_name', 'product_price', 'product_image']


admin.site.register(Product, ProductAdmin)
