from django.shortcuts import render, get_object_or_404

from .models import Product
from orderApp.forms import OrderAddProductForm


def product_detail(request, product_id):
    template = 'productApp/product.html'
    context = {
        'product': get_object_or_404(Product, id=product_id),
        'form': OrderAddProductForm(),
    }
    return render(request, template, context)
