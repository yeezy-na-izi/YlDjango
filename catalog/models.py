from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

from catalog.validators import validate_brilliant, ValidateWordsCount
from core.models import SlugMixin, PublishedMixin


class Item(PublishedMixin):
    name = models.CharField(verbose_name='Имя', max_length=150, help_text='Максимальная длинна 150')
    text = models.TextField(
        verbose_name='Описание',
        help_text='Минимум 2 слова',
        validators=[
            validate_brilliant,
            # Сделал класс для валидатора, чтобы была возможность использовать его с разным количеством слов
            # MinLengthValidator проверяет на количество символов, что не соответствует ТЗ
            ValidateWordsCount(2),
        ]
    )

    tags = models.ManyToManyField(verbose_name='Теги', to='Tag', related_name='items')
    category = models.ForeignKey(verbose_name='Категория', to='Category', related_name='items',
                                 on_delete=models.CASCADE)

    ratings = models.ManyToManyField(
        verbose_name='Оценки',
        to=User,
        related_name='items',
        through='rating.Rating',
        through_fields=('item', 'user')
    )

    class Meta(PublishedMixin.Meta):
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Tag(SlugMixin, PublishedMixin):
    class Meta(SlugMixin.Meta, PublishedMixin.Meta):
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(SlugMixin, PublishedMixin):
    weight = models.IntegerField(verbose_name='Вес', default=100, validators=[MaxValueValidator(32767), ])

    class Meta(SlugMixin.Meta, PublishedMixin.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
