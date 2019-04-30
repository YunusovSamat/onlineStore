from django.urls import re_path

from . import views

app_name = 'registrationApp'
urlpatterns = [
    re_path("^$", views.registrationForm, name='registration'),
]