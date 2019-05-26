from django.urls import re_path

from . import views

app_name = 'main'
urlpatterns = [
    re_path('^$', views.index_view, name='index'),
    re_path('^delivery_pay/$', views.delivery_pay_view, name='delivery_pay'),
]
