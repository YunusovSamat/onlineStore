from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET

from productApp.models import Product
from .order import Order
from .forms import OrderAddProductForm


@require_GET
def order_add(request, product_id):
    order = Order(request)
    product = get_object_or_404(Product, id=product_id)
    form = OrderAddProductForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        order.add(
            product=product, count=cd['count'], update_count=cd['update'],
            size=cd['size']
        )
    return redirect('orderApp:order_detail')


def order_remove(request, product_id):
    order = Order(request)
    product = get_object_or_404(Product, id=product_id)
    order.remove(product)
    return redirect('orderApp:order_detail')


def order_clear(request):
    order = Order(request)
    order.clear()
    return redirect('orderApp:order_detail')


def order_detail(request):
    order = Order(request)
    # for item in order:
    #     item['update_count_form'] = OrderAddProductForm(
    #         initial={'count': item['count'], 'update': True}
    #     )
    return render(request, 'orderApp/order.html', {'order': order})
