from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
]
