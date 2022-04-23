from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from users.models import Profile, User


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'


class MyUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    ordering = ('email',)
    list_display = ['first_name', 'last_name', 'email']


admin.site.register(User, MyUserAdmin)
