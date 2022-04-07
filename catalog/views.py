from django.shortcuts import render
from django.http import Http404
from catalog.models import Item, Category


def item_list(request):
    categories = Category.objects.published_category_and_items().order_by('weight')

    context = {'categories': categories}
    return render(request, 'catalog/all_items.html', context)


def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        raise Http404('Item does not found')
    context = {'item': item}
    return render(request, 'catalog/item_detail.html', context)
