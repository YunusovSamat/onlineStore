from django.contrib import admin

from .models import Order, ProductOrder


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'fk_user', 'name', 'surname', 'email',
        'address', 'comment', 'delivery_price', 'total', 'date'
    ]
    ordering = ['-date', 'fk_user', 'surname', 'id']
    list_filter = ['fk_user', 'surname', 'date']
    inlines = [ProductOrderInline]


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['fk_order', 'fk_product', 'count', 'size', 'id']
    ordering = ['fk_order', 'fk_product']
    list_filter = ['fk_order']


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
