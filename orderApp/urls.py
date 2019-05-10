from django.urls import re_path

from . import views

app_name = 'orderApp'
urlpatterns = [
    re_path(r'$', views.order_view, name='order'),
    re_path(r'add_to_order$', views.add_to_order, name='add_to_order')
]

