from django.contrib import auth


def get_username(request):
    return {'username': auth.get_user(request).username}
