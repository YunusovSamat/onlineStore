from django.shortcuts import render
from django.views import generic

from .models import Catalog


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    model = Catalog
    # В конце заменить текст категорий и подкатегорий в меню на данные в бд
