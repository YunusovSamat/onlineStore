from django.contrib import admin
#
from .models import ProductOrder


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['fk_client', 'date', 'finish', 'sum']
#     search_fields = ['fk_client', 'date', 'finish', 'sum']
#     ordering = ['fk_client', 'finish', 'date']
#
#
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['fk_product', 'count', 'size', 'id']
    search_fields = ['fk_product', 'count', 'size', 'id']
    ordering = ['fk_product', 'count']


# admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
