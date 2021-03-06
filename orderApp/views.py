from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse

from .order import Order
from .forms import OrderAddProductForm, OrderForUserForm, OrderForAnonymUserFrom
from . import models
from productApp.models import CountProduct


@require_GET
def order_add(request):
    order = Order(request)
    form = OrderAddProductForm(request.GET)
    data = dict()

    if form.is_valid():
        count_id = form.cleaned_data['count_id']
        count_product = get_object_or_404(CountProduct, id=count_id)
        order.add(count_product=count_product)
        data = {
            'count': order.__len__(),
            'id': count_id,
            'count_product': order.order[str(count_id)]['count'],
            'error_count': order.order[str(count_id)]['error_count'],
        }

    return JsonResponse(data, safe=False)


@require_GET
def order_delete(request):
    order = Order(request)
    form = OrderAddProductForm(request.GET)
    data = dict()
    if form.is_valid():
        count_id = form.cleaned_data['count_id']
        count_product = get_object_or_404(CountProduct, id=count_id)
        order.delete(count_product=count_product)
        data = {
            'count': order.__len__(),
            'id': count_id,
            'count_product': order.order[str(count_id)]['count'],
            'error_count': order.order[str(count_id)]['error_count'],
        }

    return JsonResponse(data, safe=False)


def order_remove(request, count_product_id):
    order = Order(request)
    order.remove(count_product_id)

    return redirect('orderApp:order_detail')


def order_clear(request):
    order = Order(request)
    order.clear()

    return redirect('orderApp:order_detail')


def order_detail(request):
    order = Order(request)
    context = {'order': order}

    return render(request, 'orderApp/order.html', context)


def checkout_view(request):
    order = Order(request)
    context = {'order': order}

    if request.user.is_authenticated:
        context['address'] = request.user.user_profile.address
        context['phone'] = request.user.user_profile.phone

    return render(request, 'orderApp/checkout.html', context)


@require_POST
def order_processing(request):
    order = Order(request)
    context = {
        'result': "",
        'id_order': "",
    }
    comment = request.POST.get('comment', '')

    if order:
        if request.user.is_authenticated:
            form = OrderForUserForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                order_model = models.Order.objects.create(
                    fk_user_id=request.user.id,
                    address=cd['address'],
                    phone=cd['phone'],
                    comment=comment,
                    delivery_price=order.get_delivery_price(),
                    total=order.get_total_delivery_price(),
                )
                for product_order in order:
                    models.ProductOrder.objects.create(
                        fk_order_id=order_model.id,
                        fk_product_id=product_order['product'].id,
                        count=product_order['count'],
                        size=product_order['size'],
                    )
                    count_product = get_object_or_404(CountProduct, id=product_order['id'])
                    count_product.count -= product_order['count']
                    count_product.save()

                order.clear()
                context['result'] = "Заказ успешно сформирован"
                context['id_order'] = order_model.id
            else:
                context['result'] = "Заказ не оформлен"

        else:
            form = OrderForAnonymUserFrom(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                order_model = models.Order.objects.create(
                    name=cd['name'],
                    surname=cd['surname'],
                    email=cd['email'],
                    address=cd['address'],
                    phone=cd['phone'],
                    comment=comment,
                    delivery_price=order.get_delivery_price(),
                    total=order.get_total_delivery_price(),
                )
                for product_order in order:
                    models.ProductOrder.objects.create(
                        fk_order_id=order_model.id,
                        fk_product_id=product_order['product'].id,
                        count=product_order['count'],
                        size=product_order['size'],
                    )
                    count_product = get_object_or_404(CountProduct, id=product_order['id'])
                    count_product.count -= product_order['count']
                    count_product.save()

                order.clear()
                context['result'] = "Заказ успешно сформирован"
                context['id_order'] = order_model.id
            else:
                context['result'] = "Заказ не оформлен"

    else:
        context['result'] = "error"

    return render(request, 'orderApp/result.html', context)



