from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import Profile, User


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'


class MyUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    fieldsets = (
        ('Конфиденциальная информация', {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name')}),
        ('Разрешения', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    ordering = ('email',)
    list_display = ['first_name', 'last_name', 'email']


admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
