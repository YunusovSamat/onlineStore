from django.shortcuts import render, get_object_or_404

from catalogApp.models import Product


def product_detail(request, slug):
    template = 'productApp/product.html'
    context = {
        'product': get_object_or_404(Product, slug=slug),
    }
    return render(request, template, context)
