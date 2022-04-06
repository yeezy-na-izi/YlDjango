from django.shortcuts import render
from catalog.models import Item, Tag
from django.db.models import Prefetch


def home(request):
    items = (
        Item.objects.filter(is_published=True).order_by('?')[:3].prefetch_related(
            Prefetch(
                'tags',
                queryset=Tag.objects.filter(is_published=True)
            )
        )
    )
    context = {'items': items}
    return render(request, 'homepage/index.html', context)
