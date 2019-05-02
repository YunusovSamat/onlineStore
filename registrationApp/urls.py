from django.urls import re_path

from . import views

app_name = 'registrationApp'
urlpatterns = [
    re_path("^$", views.signup, name='registration'),
    re_path('^login/$', views.LoginFormView.as_view()),
    re_path('^logout/$', views.LogoutView.as_view()),
]
