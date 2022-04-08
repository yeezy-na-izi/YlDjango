from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Item


def item_list(request):
    categories = Category.objects.published_category_and_items().order_by('weight')

    context = {'categories': categories}
    return render(request, 'catalog/all_items.html', context)


def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        category = item.category
        tags = item.tags.all()
    except Item.DoesNotExist:
        raise Http404('Item does not found')
    context = {
        'item': item,
        'category': category,
        'tags': tags
    }
    return render(request, 'catalog/item_detail.html', context)
