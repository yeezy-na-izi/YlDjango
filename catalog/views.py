from django.shortcuts import render, HttpResponse


def item_list(request):
    return HttpResponse('<h1>Item list</h1>')


def item_detail(request, pk):
    return HttpResponse(f'<h1> Detail item with pk = {pk}</h1>')
