from django.shortcuts import render, get_object_or_404

from .models import Product


def product_detail(request, product_id):
    template = 'productApp/product.html'
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }

    return render(request, template, context)
