from django.db.models import Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from catalog.models import Item
import django.contrib.auth.views as admin_views

from users.forms import UserForm, ProfileForm, RegistrationForm
from users.models import Profile, User


class ProfilePage(View):
    template_name = 'users/profile.html'

    def get(self, request):
        liked_items = Item.objects.user_liked_items(request.user)
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            'items': liked_items,
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            liked_items = Item.objects.user_liked_items(request.user)
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            context = {
                'items': liked_items,
                'user_form': user_form,
                'profile_form': profile_form
            }
            return render(request, self.template_name, context=context)


class UserDetail(View):
    template_name = 'users/user_detail.html'

    def get(self, request, pk):
        user = get_object_or_404(
            User.objects.only('email', 'first_name', 'last_name', 'profile__birthday').select_related('profile'),
            pk=pk
        )
        liked_items = Item.objects.user_liked_items(user)
        context = {
            'user': user,
            'items': liked_items,
        }
        return render(request, self.template_name, context=context)


class UserList(View):
    template_name = 'users/all_users.html'

    def get(self, request):
        users = User.objects.prefetch_related(
            Prefetch('profile', queryset=Profile.objects.all())
        )

        context = {
            'users': users
        }
        return render(request, self.template_name, context=context)


class SignupView(View):
    template_name = 'users/auth/signup.html'

    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


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
