from django.shortcuts import render
from django.views import generic

from .models import Catalog, Subcatalog


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    queryset = Catalog.objects.all()
    # В конце заменить текст категорий и подкатегорий в меню на данные в бд


class CatalogView(generic.DetailView):
    template_name = 'main/catalog.html'
    # queryset = Catalog.objects.all()
    # queryset = Subcatalog.objects.all()
    model = Subcatalog
    context_object_name = 'subcatalog'

