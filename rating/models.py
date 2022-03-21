from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.models import User

from catalog.models import Item


class Rating(models.Model):
    choices = (
        ('1', 'Ненависть'),
        ('2', 'Неприязнь'),
        ('3', 'Нейтрально'),
        ('4', 'Обожание'),
        ('5', 'Любовь'),
    )
    star = models.CharField(verbose_name='Оценка', max_length=1, choices=choices)
    item = models.ForeignKey(verbose_name='Товар', to='catalog.Item', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        constraints = [UniqueConstraint(fields=['item', 'user', ], name='unique_rating')]
