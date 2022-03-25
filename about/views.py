from django.shortcuts import HttpResponse


def description(request):
    return HttpResponse('<h1> description </h1>')
