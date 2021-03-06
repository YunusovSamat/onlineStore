from django.urls import re_path

from . import views

app_name = 'orderApp'
urlpatterns = [
    re_path(r'^$', views.order_detail, name='order_detail'),
    re_path(r'^add/$', views.order_add, name='order_add'),
    re_path(r'^delete/$', views.order_delete, name='order_delete'),
    re_path(r'^remove/(?P<count_product_id>\d+)/$', views.order_remove, name='order_remove'),
    re_path(r'^clear/$', views.order_clear, name='order_clear'),
    re_path(r'^checkout/$', views.checkout_view, name='checkout_view'),
    re_path(r'^order_processing/$', views.order_processing, name='order_processing'),
]
