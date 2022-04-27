import random

from django.views.generic import TemplateView

from catalog.models import Item


class HomeView(TemplateView):
    template_name = 'homepage/index.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ids = list(Item.objects.filter(is_published=True).values_list('pk', flat=True))
        random.shuffle(ids)
        items = Item.objects.published_item_and_tags().filter(id__in=ids[:3])

        context['items'] = items
        return context
