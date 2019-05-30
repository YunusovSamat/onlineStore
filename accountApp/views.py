from django.contrib import auth
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf

from .form import SignUpForm
from .models import UserProfile


def signup(request):
    template = 'accountApp/signup.html'
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        if user_form.is_valid() and address and phone:
            user_form.save()
            username = user_form.cleaned_data.get('username')
            my_password = user_form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=my_password)
            auth.login(request, user)

            UserProfile.objects.create(
                fk_user_id=user.id, address=address, phone=phone
            )

            return redirect('main:index')
    else:
        user_form = SignUpForm()

    return render(request, template, {'user_form': user_form})


def login(request):
    template = 'accountApp/login.html'
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
            context['login_error'] = "Неправильный логин или пароль"
            return render_to_response(template, context)
    else:
        return render_to_response(template, context)


def logout(request):
    auth.logout(request)
    return redirect("main:index")
