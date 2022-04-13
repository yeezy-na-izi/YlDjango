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


class TagManager(models.Manager):
    def published_tags(self):
        return self.filter(is_published=True)
