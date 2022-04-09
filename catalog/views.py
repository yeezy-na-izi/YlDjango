from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Item


def item_list(request):
    template_name = 'catalog/all_items.html'

    categories = Category.objects.published_category_and_items().order_by('weight')

    context = {'categories': categories}

    return render(request, template_name, context)


def item_detail(request, pk):
    template_name = 'catalog/item_detail.html'

    item = get_object_or_404(Item.objects.published_item_and_tags().select_related('category'), pk=pk)
    context = {'item': item}

    return render(request, template_name, context)
