from django.db.models import Prefetch
from django.shortcuts import render
from django.http import Http404
from catalog.models import Item, Tag

from django.shortcuts import get_object_or_404


def item_list(request):
    items = Item.objects.filter(is_published=True).prefetch_related(
        Prefetch(
            'tags',
            queryset=Tag.objects.filter(is_published=True)
        )
    )
    context = {'items': items}
    return render(request, 'catalog/all_items.html', context)


def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        raise Http404('Item does not found')
    context = {'item': item}
    return render(request, 'catalog/item_detail.html', context)
