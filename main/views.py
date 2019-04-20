from django.shortcuts import render
from django.views import generic

from .models import Catalog


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    model = Catalog


class CatalogView(generic.DetailView):
    template_name = 'main/catalog.html'
    model = Catalog
    context_object_name = 'subcatalog'
