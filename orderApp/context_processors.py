from .order import Order


def get_order(request):
    return {
        'order_len': Order(request).__len__(),
    }
