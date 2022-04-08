from django.contrib.auth.models import User
from django.db import models
from django.db.models import Prefetch

from catalog.validators import ValidateWordsCount, validate_brilliant
from core.models import PublishedMixin, SlugMixin


class CategoryManager(models.Manager):
    def published_category_and_items(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch(
                'items',
                queryset=Item.objects.published_item_and_tags()
            )
        )


class ItemManager(models.Manager):
    def published_item_and_tags(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch(
                'tags',
                queryset=Tag.objects.published_tags(),
            )
        )


class TagManager(models.Manager):
    def published_tags(self):
        return self.filter(is_published=True)


class Item(PublishedMixin):
    name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        help_text='Максимальная длинна 150'
    )
    text = models.TextField(
        verbose_name='Описание',
        help_text='Минимум 2 слова',
        validators=[
            validate_brilliant,
            # Сделал класс для валидатора,
            # возможность использовать его с разным количеством слов
            # MinLengthValidator проверяет на количество символов,
            # что не соответствует ТЗ
            ValidateWordsCount(2),
        ]
    )

    tags = models.ManyToManyField(
        verbose_name='Теги',
        to='Tag',
        related_name='items'
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to='Category',
        related_name='items',
        null=True,
        on_delete=models.SET_NULL
    )

    ratings = models.ManyToManyField(
        verbose_name='Оценки',
        to=User,
        related_name='items',
        through='rating.Rating',
        through_fields=('item', 'user')
    )

    objects = ItemManager()

    class Meta(PublishedMixin.Meta):
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Tag(SlugMixin, PublishedMixin):
    name = models.CharField(verbose_name='Имя', max_length=255, default='')
    objects = TagManager()

    class Meta(SlugMixin.Meta, PublishedMixin.Meta):
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Category(SlugMixin, PublishedMixin):
    name = models.CharField(verbose_name='Имя', max_length=255, default='')
    weight = models.PositiveSmallIntegerField(verbose_name='Вес', default=100)

    objects = CategoryManager()

    class Meta(SlugMixin.Meta, PublishedMixin.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
