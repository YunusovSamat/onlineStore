from django.shortcuts import render


def index_view(request):
    return render(request, 'main/index.html')


def delivery_pay_view(request):
    return render(request, 'main/delivery_pay.html')
