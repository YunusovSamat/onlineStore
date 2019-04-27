from django.urls import re_path

from . import views

app_name = 'productApp'
urlpatterns = [
    re_path(r'^$', views.product_detail, name='product'),
]
