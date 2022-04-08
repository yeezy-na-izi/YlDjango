import random

from django.shortcuts import render

from catalog.models import Item


def home(request):
    template_name = 'homepage/index.html'
    # fasted than order_by('?')
    ids = list(Item.objects.filter(is_published=True).values_list('pk', flat=True))
    random.shuffle(ids)
    items = Item.objects.published_item_and_tags().filter(id__in=ids[:3])
    context = {'items': items}

    return render(request, template_name, context)
