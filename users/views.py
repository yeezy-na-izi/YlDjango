from django.shortcuts import render


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

    context = {}

    return render(request, template_name, context)


def profile(request):
    template_name = 'users/profile.html'

    context = {}

    return render(request, template_name, context)
