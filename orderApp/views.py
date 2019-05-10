from django.shortcuts import render, get_object_or_404


def order_view(request):
    template = 'orderApp/order.html'

    return render(request, template)


def add_to_order(request):
    # if request.method == 'POST':
    return request(request)
