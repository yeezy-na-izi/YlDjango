from django.db import models
from catalog.validators import validate_brilliant, ValidateWordsCount
from django.core.validators import MaxValueValidator
from core.models import AbstractTag
from django.contrib.auth.models import User


class Item(models.Model):
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
    is_published = models.BooleanField(verbose_name='Опубликованно', default=True)
    tags = models.ManyToManyField(verbose_name='Теги', to='Tag', related_name='items')

    category = models.ForeignKey(verbose_name='Категория', to='Category', related_name='items',
                                 on_delete=models.CASCADE)

    ratings = models.ManyToManyField(verbose_name='Оценки', to=User, through='rating.Rating', related_name='items')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'


class Tag(AbstractTag):
    name = models.CharField(verbose_name='name', max_length=120)

    class Meta(AbstractTag.Meta):
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(AbstractTag):
    weight = models.IntegerField(verbose_name='Вес', default=100, validators=[MaxValueValidator(32767), ])

    class Meta(AbstractTag.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
