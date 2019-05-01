from django.urls import re_path, include

from . import views

app_name = 'main'
urlpatterns = [
    re_path('^$', views.index_view, name='index'),
]
