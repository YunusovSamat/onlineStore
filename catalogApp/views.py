from django.shortcuts import render, get_object_or_404

from .models import Subcatalog
from .forms import CatalogFilterForm


def catalog_list(request, subcatalog_id):
    template = 'catalogApp/catalog.html'
    subcatalog = get_object_or_404(Subcatalog, id=subcatalog_id)
    products = subcatalog.products.all()
    form = CatalogFilterForm(request.GET)

    if form.is_valid():
        cd = form.cleaned_data['sort']
        if cd:
            products = products.order_by(cd)

    context = {
        'subcatalog_name': subcatalog.name,
        'products': products,
        'form': form,
    }

    return render(request, template, context)

