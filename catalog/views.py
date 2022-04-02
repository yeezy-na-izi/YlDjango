from django.shortcuts import render


def item_list(request):
    context = {}

    return render(request, 'catalog/all_items.html', context)


def item_detail(request, pk):
    context = {'id': pk}

    return render(request, 'catalog/item_detail.html', context)
