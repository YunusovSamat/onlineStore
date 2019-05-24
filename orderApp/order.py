from decimal import Decimal

from django.shortcuts import get_object_or_404
from django.conf import settings
from productApp.models import Product


class Order(object):
    def __init__(self, request):
        self.session = request.session
        order = self.session.get(settings.CART_SESSION_ID)
        if not order:
            order = self.session[settings.CART_SESSION_ID] = {}
        self.order = order

    def add(self, count_product):
        count_product_id = str(count_product.id)

        if count_product_id not in self.order:
            self.order[count_product_id] = {
                'id': count_product.id,
                'count': 0,
                'price': str(count_product.fk_product.price),
                'size': count_product.fk_size.size,
            }

        if self.order[count_product_id]['count'] + 1 <= count_product.count:
            self.order[count_product_id]['count'] += 1
        else:
            self.order[count_product_id]['count'] = count_product.count
            self.order[count_product_id]['error_count'] = "превышен лимит количества"
        self.save()

    def delete(self, count_product):
        count_product_id = str(count_product.id)

        # if count_product_id in self.order:


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.order
        self.session.modified = True

    def remove(self, count_product_id):
        count_product_id = str(count_product_id)
        if count_product_id in self.order:
            del self.order[count_product_id]
            self.save()

    def __iter__(self):
        count_product_ids = self.order.keys()

        for count_product_id in count_product_ids:
            product = get_object_or_404(Product, counts__id=count_product_id)
            self.order[str(count_product_id)]['product'] = product

        for item in self.order.values():
            item['total_price'] = Decimal(item['price']) * item['count']
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.order.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['count'] for item in self.order.values())

    def get_delivery_price(self):
        if self.get_total_price() >= 5000:
            return 0
        else:
            return 490

    def get_total_delivery_price(self):
        return self.get_total_price() + self.get_delivery_price()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
