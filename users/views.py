from django.shortcuts import render


def user_list(request):
    context = {}

    return render(request, 'users/all_users.html', context)


def user_detail(request, pk):
    context = {'id': pk}

    return render(request, 'users/user_detail.html', context)


def signup(request):
    context = {}

    return render(request, 'users/signup.html', context)


def profile(request):
    context = {}

    return render(request, 'users/profile.html', context)
