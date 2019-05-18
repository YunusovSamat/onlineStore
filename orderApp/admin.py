from django.contrib import admin

from .models import Order, ProductOrder


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'fk_user', 'name', 'surname', 'email', 'date',
        'address', 'comment', 'delivery_price', 'total'
    ]
    search_fields = [
        'fk_user', 'name', 'surname', 'email', 'date',
        'address', 'comment', 'total'
    ]
    ordering = ['date', 'fk_user', 'surname']
    inlines = [ProductOrderInline]


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['fk_order', 'fk_product', 'count', 'size', 'id']
    search_fields = ['fk_order', 'fk_product', 'count', 'size', 'id']
    ordering = ['fk_order', 'fk_product']


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
