from django.urls import path, re_path

from . import views

app_name = 'main'
urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path(
        r'^catalog/(?P<slug>\w+)/$', views.CatalogView.as_view(), name='catalog'),
]
