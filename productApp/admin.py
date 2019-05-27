from django.contrib import admin

from .models import Product, SizeProduct, CountProduct, ImageProduct
from .models import ColorProduct, ProductJoinColor


class CountProductInline(admin.TabularInline):
    model = CountProduct
    extra = 5


class ImageProductInline(admin.StackedInline):
    model = ImageProduct
    extra = 5


class ProductJoinColorInline(admin.TabularInline):
    model = ProductJoinColor
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'fk_subcatalog', 'name', 'price', 'old_price', 'description',
        'new', 'id'
    ]
    ordering = ['fk_subcatalog', 'name', 'price', 'id']
    list_filter = ['fk_subcatalog']
    inlines = [CountProductInline, ImageProductInline, ProductJoinColorInline]


class SizeProductAdmin(admin.ModelAdmin):
    list_display = ['size', 'id']
    ordering = ['size']


class CountProductAdmin(admin.ModelAdmin):
    list_display = ['fk_product', 'fk_size', 'count', 'id']
    ordering = ['fk_product', 'fk_size', 'count']


class ImageProductAdmin(admin.ModelAdmin):
    list_display = ['fk_product', 'image', 'id']
    ordering = ['fk_product', 'image']


class ColorProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'id']
    ordering = ['name']
    inlines = [ProductJoinColorInline]


class ProductJoinColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'fk_product', 'fk_color_product']
    ordering = ['fk_product', 'fk_color_product']


admin.site.register(Product, ProductAdmin)
admin.site.register(SizeProduct, SizeProductAdmin)
admin.site.register(CountProduct, CountProductAdmin)
admin.site.register(ImageProduct, ImageProductAdmin)
admin.site.register(ColorProduct, ColorProductAdmin)
admin.site.register(ProductJoinColor, ProductJoinColorAdmin)
