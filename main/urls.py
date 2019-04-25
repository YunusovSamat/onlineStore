from django.urls import re_path, include

from . import views

app_name = 'main'
urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path(r'^catalog/(?P<slug>\w+)/$', include('catalogApp.urls'), name='catalog2'),
]
