from django.shortcuts import render
from catalog.models import Item


def home(request):
    items = Item.objects.published_item_and_tags().order_by('?')[:3]
    context = {'items': items}
    return render(request, 'homepage/index.html', context)
