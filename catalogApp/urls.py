from django.urls import re_path

from . import views

app_name = 'catalogApp'
urlpatterns = [
    re_path('^$', views.CatalogView.as_view(), name='catalog'),
    # re_path(),
]

