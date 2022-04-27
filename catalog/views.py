from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Avg, Count
from django.views.generic import View

from catalog.models import Category, Item
from rating.models import Rating


class ItemList(View):
    template_name = 'catalog/all_items.html'

    def get(self, request):
        categories = Category.objects.published_category_and_items().order_by('weight')

        context = {'categories': categories}

        return render(request, self.template_name, context)


class ItemDetail(View):
    template_name = 'catalog/item_detail.html'
    items = Item.objects.published_item_and_tags()

    def get(self, request, pk):
        stars_variants = Rating.choices

        item = get_object_or_404(self.items, pk=pk)
        stars = item.item_stars.exclude(star=0).aggregate(Avg('star'), Count('star'))

        user_star = 0
        if request.user.is_authenticated:
            user_rate = Rating.objects.filter(item=item, user=request.user).first()
            if user_rate:
                user_star = user_rate.star

        context = {
            'item': item,
            'stars_variants': stars_variants,
            'stars': stars,
            'user_star': user_star
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        item = get_object_or_404(self.items, pk=pk)

        if 'rate' in request.POST and request.POST['rate'].isdigit():
            rate = int(request.POST['rate'])

            if rate in dict(Rating.choices).keys() and request.user.is_authenticated:
                Rating.objects.update_or_create(
                    item=item,
                    user=request.user,
                    defaults={'star': rate}
                )
        return redirect('item_detail', pk=pk)
