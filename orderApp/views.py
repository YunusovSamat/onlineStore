from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST

from productApp.models import CountProduct
from .order import Order
from .forms import OrderAddProductForm


@require_GET
def order_add(request):
    order = Order(request)
    form = OrderAddProductForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        count_product = get_object_or_404(CountProduct, id=cd['count_id'])
        count = cd['count']
        order.add(count_product=count_product, count=count)
    return redirect('orderApp:order_detail')


def order_remove(request, count_product_id):
    order = Order(request)
    # count_product = get_object_or_404(CountProduct, id=count_product_id)
    order.remove(count_product_id)
    return redirect('orderApp:order_detail')


def order_clear(request):
    order = Order(request)
    order.clear()
    return redirect('orderApp:order_detail')


def order_detail(request):
    order = Order(request)
    return render(request, 'orderApp/order.html', {'order': order})


# @require_POST
# def order_processing(request):
#     order = Order(request)
#
#     if request.user.is_authenticated():
#
#     else:
#
