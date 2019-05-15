from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST

from productApp.models import CountProduct
from .order import Order
from .forms import OrderAddProductForm, OrderForUserForm, OrderForAnonymUserFrom
from . import models
from productApp.models import CountProduct


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


@require_POST
def order_processing(request):
    order = Order(request)
    id = ""

    # if order is not None:
    #     if request.user.is_authenticated:
    #         form = OrderForUserForm(request.POST)
    #         if form.is_valid():
    #             cd = form.cleaned_data
    #             order_model = models.Order.objects.create(
    #                 fk_user_id=request.user.id,
    #                 address=cd['address'],
    #                 comment=cd['comment'],
    #                 total=order.get_total_price(),
    #             )
    #             for product_order in order:
    #                 models.ProductOrder.objects.create(
    #                     fk_order_id=order_model.id,
    #                     fk_product_id=product_order['product'].id,
    #                     count=product_order['count'],
    #                     size=product_order['size'],
    #                 )
    #                 count_product = get_object_or_404(CountProduct, id=product_order['id'])
    #                 count_product.count -= product_order['count']
    #                 count_product.save()
    #
    #             order.clear()
    #             result = "Заказ успешно оформлен"
    #             id = order_model.id
    #         else:
    #             result = "Заказ не оформлен"
    #
    #     else:
    #         form = OrderForAnonymUserFrom(request.POST)
    #         if form.is_valid():
    #             cd = form.cleaned_data
    #             order_model = models.Order.objects.create(
    #                 name=cd['name'],
    #                 surname=cd['surname'],
    #                 email=cd['email'],
    #                 address=cd['address'],
    #                 comment=cd['comment'],
    #                 total=order.get_total_price(),
    #             )
    #             for product_order in order:
    #                 models.ProductOrder.objects.create(
    #                     fk_order_id=order_model.id,
    #                     fk_product_id=product_order['product'].id,
    #                     count=product_order['count'],
    #                     size=product_order['size'],
    #                 )
    #                 count_product = get_object_or_404(CountProduct, id=product_order['id'])
    #                 count_product.count -= product_order['count']
    #                 count_product.save()
    #
    #             order.clear()
    #             result = "Заказ успешно оформлен"
    #             id = order_model.id
    #         else:
    #             result = "Заказ не оформлен"
    #
    #     context = {
    #         'result': result,
    #         'id': id,
    #     }

    context = {'result': order}
    return render(request, 'orderApp/result.html', context)

