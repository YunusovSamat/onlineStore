from django.shortcuts import render


def index_view(request):
    template = 'main/index.html'

    return render(request, template)


def delivery_pay_view(request):
    template = 'main/delivery_pay.html'

    return render(request, template)
