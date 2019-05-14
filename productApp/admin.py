from django.contrib import admin

from .models import Product, SizeProduct, CountProduct, ImageProduct


class CountProductInline(admin.TabularInline):
    model = CountProduct


class ImageProductInline(admin.StackedInline):
    model = ImageProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['fk_subcatalog', 'id', 'name', 'description', 'price']
    search_fields = ['fk_subcatalog', 'id', 'name', 'description', 'price']
    ordering = ['fk_subcatalog', 'id']
    inlines = [CountProductInline, ImageProductInline]


class SizeProductAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']
    ordering = ['size']


class CountProductAdmin(admin.ModelAdmin):
    list_display = ['fk_product', 'fk_size', 'count', 'id']
    search_fields = ['fk_product', 'fk_size', 'count']
    ordering = ['fk_product', 'fk_size', 'count']


class ImageProductAdmin(admin.ModelAdmin):
    list_display = ['fk_product', 'image']
    search_fields = ['fk_product', 'image']
    ordering = ['fk_product', 'image']


admin.site.register(Product, ProductAdmin)
admin.site.register(SizeProduct, SizeProductAdmin)
admin.site.register(CountProduct, CountProductAdmin)
admin.site.register(ImageProduct, ImageProductAdmin)
