from decimal import Decimal

from django.conf import settings
from productApp.models import Product


class Order(object):
    def __init__(self, request):
        self.session = request.session
        order = self.session.get(settings.CART_SESSION_ID)
        if not order:
            order = self.session[settings.CART_SESSION_ID] = {}
        self.order = order

    def add(self, product, count=1, update_count=False, size=46):
        product_id = str(product.id)

        if product_id not in self.order:
            self.order[product_id] = {'count': 0, 'price': str(product.price), 'size': size}

        self.order[product_id] = {'count': 0, 'price': str(product.price), 'size': size}
        if update_count:
            self.order[product_id]['count'] = count
        else:
            self.order[product_id]['count'] += count
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.order
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.order:
            del self.order[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.order.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.order[str(product.id)]['product'] = product

        for item in self.order.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['count']
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.order.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['count'] for item in self.order.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
