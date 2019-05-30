from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile


class UserInline(admin.TabularInline):
    model = UserProfile


class UserAdmin(UserAdmin):
    list_display = [
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'user_profile'
    ]
    inlines = (UserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
