from django.urls import re_path

from . import views

app_name = 'orderApp'
urlpatterns = [
    re_path(r'$', views.order_view, name='order'),
]
