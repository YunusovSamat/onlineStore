from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth

from .form import SignUpForm


def signup(request):
    template = 'accountApp/signup.html'
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=my_password)
            auth.login(request, user)
            return redirect('main:index')
    else:
        form = SignUpForm()

    return render(request, template, {'form': form})


def login(request):
    context = {}
    context.update(csrf(request))

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:index')
        else:
            context['login_error'] = "error"
            return render_to_response('accountApp/login.html', context)
    else:
        return render_to_response('accountApp/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect("main:index")
