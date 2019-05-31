from django.contrib import admin

from .models import Order, ProductOrder


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'fk_user', 'surname',
        'phone', 'total', 'date'
    ]
    ordering = ['-id', 'fk_user', 'surname']
    list_filter = ['fk_user', 'surname', 'date']
    inlines = [ProductOrderInline]


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['fk_order', 'fk_product', 'count', 'size', 'id']
    ordering = ['fk_order', 'fk_product']
    list_filter = ['fk_order']


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
