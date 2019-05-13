from decimal import Decimal

from django.conf import settings
from orderApp.models import ProductOrder


class Order(object):
    def __init__(self, request):
        self.session = request.session
        order = self.session.get(settings.CART_SESSION_ID)
        if not order:
            order = self.session[settings.CART_SESSION_ID] = {}
        self.order = order

    def add(self, product_order):
        product_order_id = str(product_order.id)

        if product_order_id not in self.order:
            self.order[product_order_id] = {
                'price': str(product_order.fk_product.price),
                'size': product_order.size
            }
        self.order[product_order_id]['count'] = product_order.count
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.order
        self.session.modified = True

    # def remove(self, product):
    #     product_id = str(product.id)
    #     if product_id in self.order:
    #         del self.order[product_id]
    #         self.save()

    def __iter__(self):
        product_order_ids = self.order.keys()
        products_order = ProductOrder.objects.filter(id__in=product_order_ids)
        for product_order in products_order:
            self.order[str(product_order.id)]['product_order'] = product_order

        for item in self.order.values():
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['count'] for item in self.order.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
