from .order import Order


def get_order(request):
    return {'order': Order(request)}
