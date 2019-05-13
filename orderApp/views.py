from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET

from productApp.models import Product
from .order import Order
from .forms import OrderAddProductForm
from .models import ProductOrder


@require_GET
def order_add(request):
    order = Order(request)
    form = OrderAddProductForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        # product_order = ProductOrder.objects.get_or_create(
        #     fk_product_id=cd['product_id'],
        #     size=cd['size'],
        #     defaults={'count': cd['count']},
        # )[0]
        try:
            product_order = ProductOrder.objects.get(
                fk_product_id=cd['product_id'], size=cd['size']
            )
            product_order.count += 1
            product_order.save()
        except ProductOrder.DoesNotExist:
            product_order = ProductOrder.objects.create(
                fk_product_id=cd['product_id'], count=cd['count'],
                size=cd['size']
            )
        order.add(product_order=product_order)
    return redirect('orderApp:order_detail')


# def order_remove(request, product_id):
#     order = Order(request)
#     product = get_object_or_404(Product, id=product_id)
#     order.remove(product)
#     return redirect('orderApp:order_detail')


def order_clear(request):
    order = Order(request)
    order.clear()
    return redirect('orderApp:order_detail')


def order_detail(request):
    order = Order(request)
    return render(request, 'orderApp/order.html', {'order': order})
