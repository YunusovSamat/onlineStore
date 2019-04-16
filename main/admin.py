from django.contrib import admin

from .models import Catalog, Subcatalog, Product, ImageProduct


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
        'product_count', 'product_description'
    ]
    search_fields = ['product_name', 'product_price']


admin.site.register(Product, ProductAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_product_name', 'image_product_product']
    search_fields = ['image_product_name', 'image_product_product']


admin.site.register(ImageProduct, ImageAdmin)
