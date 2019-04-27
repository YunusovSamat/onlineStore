from django.urls import re_path, include

from . import views

app_name = 'catalogApp'
urlpatterns = [
    re_path(r'^$', views.catalog_list, name='catalog'),
]

