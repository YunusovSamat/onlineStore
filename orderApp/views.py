from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from catalogApp.models import Product
from .order import Order
from .forms import OrderAddProductForm


@require_POST
def order_add(request, product_id):
    order = Order(request)
    product = get_object_or_404(Product, id=product_id)
    form = OrderAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        order.add(porduct=product, count=cd['count'], update_count=cd['update'])
    return redirect('orderApp:order_detail')


def order_remove(request, product_id):
    order = Order(request)
    product = get_object_or_404(Product, id=product_id)
    order.remove(product)
    return redirect('orderApp:order_detail')


def order_detail(request):
    order = Order(request)
    for item in order:
        item['update_count_form'] = OrderAddProductForm(
            initial={'count': item['count'], 'update': True}
        )
    return render(request, 'orderApp/order.html', {'order': order})
