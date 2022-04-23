from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from catalog.models import Item
import django.contrib.auth.views as admin_views

from users.forms import UserForm, ProfileForm, RegistrationForm


@login_required
def profile(request):
    template_name = 'users/profile.html'
    liked_items = Item.objects.user_liked_items(request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'items': liked_items,
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, template_name, context=context)


def user_list(request):
    template_name = 'users/all_users.html'

    context = {}

    return render(request, template_name, context)


def user_detail(request, pk):
    template_name = 'users/user_detail.html'

    context = {'id': pk}

    return render(request, template_name, context)


def signup(request):
    template_name = 'users/signup.html'

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form}

    return render(request, template_name, context)


# Django auth views
class LoginView(admin_views.LoginView):
    template_name = 'users/auth/login.html'


class PasswordChangeDoneView(admin_views.PasswordChangeDoneView):
    template_name = 'users/auth/password_change_done.html'


class LogoutView(admin_views.LogoutView):
    template_name = 'users/auth/logout.html'


class PasswordResetView(admin_views.PasswordResetView):
    template_name = 'users/auth/password_reset.html'


class PasswordResetDoneView(admin_views.PasswordResetDoneView):
    template_name = 'users/auth/password_reset_done.html'


class PasswordResetConfirmView(admin_views.PasswordResetConfirmView):
    template_name = 'users/auth/reset.html'


class PasswordResetCompleteView(admin_views.PasswordResetCompleteView):
    template_name = 'users/auth/reset_done.html'


class PasswordChangeView(admin_views.PasswordChangeView):
    template_name = 'users/auth/password_change.html'
