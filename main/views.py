from django.shortcuts import render
from django.views import generic

from .models import Catalog


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'catalogs'
    model = Catalog

