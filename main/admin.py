from django.contrib import admin

from .models import Catalog, Subcatalog, Product, SizeProduct, CountProduct, \
    ImageProduct, ImagePage


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    search_fields = ['slug', 'name']
    ordering = ['slug']


class SubcatalogAdmin(admin.ModelAdmin):
    list_display = ['fk_catalog', 'slug', 'name']
    search_fields = ['fk_catalog', 'slug', 'name']
    ordering = ['fk_catalog', 'slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['fk_subcatalog', 'slug', 'name', 'description', 'price']
    search_fields = ['fk_subcatalog', 'slug', 'name', 'description', 'price']
    ordering = ['fk_subcatalog', 'slug']


class SizeProductAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']
    ordering = ['size']


class CountProductAdmin(admin.ModelAdmin):
    list_display = ['fk_product', 'fk_size', 'count']
    search_fields = ['fk_product', 'fk_size', 'count']
    ordering = ['fk_product', 'fk_size', 'count']


class ImageProductAdmin(admin.ModelAdmin):
    list_display = ['fk_product', 'slug', 'image']
    search_fields = ['fk_product', 'slug', 'image']
    ordering = ['fk_product', 'image']


class ImagePageAdmin(admin.ModelAdmin):
    list_display = ['slug', 'image']
    search_fields = ['slug', 'image']
    ordering = ['image']


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Subcatalog, SubcatalogAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SizeProduct, SizeProductAdmin)
admin.site.register(CountProduct, CountProductAdmin)
admin.site.register(ImageProduct, ImageProductAdmin)
admin.site.register(ImagePage, ImagePageAdmin)
