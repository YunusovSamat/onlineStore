# from django.contrib import admin
#
# from .models import Order, ProductOrder


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['fk_client', 'date', 'finish', 'sum']
#     search_fields = ['fk_client', 'date', 'finish', 'sum']
#     ordering = ['fk_client', 'finish', 'date']
#
#
# class ProductOrderAdmin(admin.ModelAdmin):
#     list_display = ['fk_order', 'fk_product', 'count', 'size']
#     search_fields = ['fk_order', 'fk_product', 'count', 'size']
#     ordering = ['fk_order', 'fk_product', 'count', 'size']
#
#
# admin.site.register(Order, OrderAdmin)
# admin.site.register(ProductOrder, ProductOrderAdmin)
