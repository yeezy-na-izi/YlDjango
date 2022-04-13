from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from users.forms import LoginUserForm


def user_list(request):
    template_name = 'users/all_users.html'

    context = {}

    return render(request, template_name, context)


def user_detail(request, pk):
    template_name = 'users/user_detail.html'

    context = {'id': pk}

    return render(request, template_name, context)


@require_POST
def signup(request):
    form = LoginUserForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)

    return redirect(request.POST['from'])


def profile(request):
    template_name = 'users/profile.html'

    context = {}

    return render(request, template_name, context)
