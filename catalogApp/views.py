from django.shortcuts import render, get_object_or_404

from .models import Subcatalog


def catalog_list(request, subcatalog_id):
    template = 'catalogApp/catalog.html'
    subcatalog = get_object_or_404(Subcatalog, id=subcatalog_id)
    products = subcatalog.products.all()
    sale = request.GET.getlist('sale', [None])[0]
    new = request.GET.getlist('new', [None])[0]
    sort_price = request.GET.get('sort', False)

    if sale:
        products = products.filter(old_price__gt=0)

    if new:
        products = products.filter(new=True)

    if sort_price:
        if sort_price == 'min_price':
            products = products.order_by('price')
        elif sort_price == 'max_price':
            products = products.order_by('-price')
    context = {
        'subcatalog_name': subcatalog.name,
        'subcatalog_id': subcatalog.id,
        'products': products,
        'sale': sale,
        'new': new,
        'sort_price': sort_price,
    }

    return render(request, template, context)

