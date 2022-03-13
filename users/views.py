from django.shortcuts import render, HttpResponse


def user_list(request):
    return HttpResponse('<h1>User list</h1>')


def user_detail(request, pk):
    return HttpResponse(f'<h1>User detail pk={pk}</h1>')


def signup(request):
    return HttpResponse('<h1>Signup</h1>')


def profile(request):
    return HttpResponse('<h1>Profile</h1>')
