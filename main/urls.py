from django.urls import re_path, include

from . import views

app_name = 'main'
urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
]
