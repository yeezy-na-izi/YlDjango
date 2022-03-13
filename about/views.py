from django.shortcuts import render, HttpResponse


def description(request):
    return HttpResponse('<h1> description </h1>')
