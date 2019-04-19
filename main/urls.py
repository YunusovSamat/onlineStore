from django.urls import re_path

from . import views

app_name = 'main'
urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path(r'^catalog/$', views.CatalogView.as_view(), name='catalog'),
]
