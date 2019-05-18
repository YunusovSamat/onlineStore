from django.contrib import auth


def get_username(request):
    return {
        # 'username': auth.get_user(request).username,
        'is_auth': auth.get_user(request).is_authenticated,
    }
