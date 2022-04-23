from django.db.models import Prefetch
from django.db import models
from django.apps import apps


class CategoryManager(models.Manager):
    def published_category_and_items(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch(
                'items',
                queryset=apps.get_model('catalog.Item').objects.published_item_and_tags()
            )
        )


class ItemManager(models.Manager):
    def published_item_and_tags(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch(
                'tags',
                queryset=apps.get_model('catalog.Tag').objects.published_tags(),
            )
        )

    def user_liked_items(self, user):
        return self.filter(
            pk__in=apps.get_model('rating.Rating').objects.filter(
                user=user, star=5).values_list('item_id')
        ).prefetch_related(
            Prefetch('tags', queryset=apps.get_model('catalog.Tag').objects.published_tags())
        ).only('name', 'text', 'tags__name', 'category_id')


class TagManager(models.Manager):
    def published_tags(self):
        return self.filter(is_published=True)
