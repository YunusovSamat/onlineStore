from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from .form import SignUpForm
from .models import UserProfile


def signup(request):
    context = {'signup_errors': ''}

    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        if user_form.is_valid() and address and phone:
            user_form.save()
            cd = user_form.cleaned_data
            username = cd['username']
            my_password = cd['password1']
            user = auth.authenticate(username=username, password=my_password)
            auth.login(request, user)

            UserProfile.objects.create(
                fk_user_id=user.id, address=address, phone=phone
            )
            return JsonResponse(context)
        else:
            errors = "Ошибка"
            for x in user_form.errors:
                errors += str(user_form.errors.get(x))
            context['signup_errors'] = errors
            return JsonResponse(context)
    else:
        return HttpResponse("")


def login(request):
    context = {'login_error': ''}

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return JsonResponse(context)
        else:
            context['login_error'] = "Неправильный логин или пароль"
            return JsonResponse(context)
    else:
        return HttpResponse("")


def logout(request):
    auth.logout(request)
    return redirect("main:index")
