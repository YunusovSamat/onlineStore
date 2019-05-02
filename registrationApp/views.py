from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .form import SignUpForm


def signup(request):
    template = 'registrationApp/registration.html'
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('main:index')
    else:
        form = SignUpForm()

    return render(request, template, {'form': form})


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'base_template.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)

        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect("/")
