from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Avg, Count
from django.views.generic import View

from catalog.models import Category, Item
from rating.models import Rating


def item_list(request):
    template_name = 'catalog/all_items.html'

    categories = Category.objects.published_category_and_items().order_by('weight')

    context = {'categories': categories}

    return render(request, template_name, context)


class ItemDetail(View):
    template_name = 'catalog/item_detail.html'
    items = Item.objects.published_item_and_tags()

    def get(self, request, pk):
        star_dict = Rating.choices
        item = get_object_or_404(self.items, pk=pk)
        stars = Rating.objects.filter(item=item, star__in=[1, 2, 3, 4, 5]).aggregate(Avg('star'), Count('star'))
        if request.user.is_authenticated:
            try:
                user_star = Rating.objects.get(item=item, user=request.user).star
            except Rating.DoesNotExist:
                user_star = 0
        else:
            user_star = 0
        context = {
            'item': item,
            'star_dict': star_dict,
            'stars': stars,
            'user_star': user_star
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        item = get_object_or_404(self.items, pk=pk)
        if request.POST['rate'] in ['0', '1', '2', '3', '4', '5'] and request.user.is_authenticated:
            obj, created = Rating.objects.get_or_create(
                user=request.user,
                item=item,
                defaults={
                    'item': item,
                    'user': request.user,
                }
            )

            obj.star = int(request.POST['rate'])
            obj.save()
        return redirect('item_detail', pk=pk)
