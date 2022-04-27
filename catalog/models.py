from users.models import User
from django.db import models

from catalog.managers import ItemManager, TagManager, CategoryManager
from catalog.validators import ValidateWordsCount, validate_brilliant
from core.models import PublishedMixin, SlugMixin

from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe


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

    image = models.ImageField(
        upload_to='uploads/',
        verbose_name='Изображение',
        null=True
    )

    def get_image_x1280(self):
        return get_thumbnail(self.image, '1280', quality=51)
    

    def get_image_400x300(self):
        return get_thumbnail(self.image, '400x300', crop='center', quality=51)
    
    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50">')
        return 'Нет изображения'
    
    image_tmb.short_descriptions = 'Превью'
    image_tmb.allow_tags = True

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


class Gallery(models.Model):
    image = models.ImageField(
        upload_to='uploads/',
        verbose_name='Изображение'
    )

    item = models.ForeignKey(
        verbose_name='Товар',
        to='Item',
        related_name='gallery',
        on_delete=models.CASCADE
    )

    class Meta():
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
