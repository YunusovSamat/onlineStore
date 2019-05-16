from django.shortcuts import render, get_object_or_404

from .models import Product


def product_detail(request, product_id):
    template = 'productApp/product.html'
    context = {
        'product': get_object_or_404(Product, id=product_id),
    }

    return render(request, template, context)
