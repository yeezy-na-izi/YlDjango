from django.db import models
from catalog.models import Item
from django.contrib.auth.models import User


class Rating(models.Model):
    choices = (
        ('1', 'Ненависть'),
        ('2', 'Неприязнь'),
        ('3', 'Нейтрально'),
        ('4', 'Обожание'),
        ('5', 'Любовь'),
    )
    star = models.CharField(verbose_name='Оценка', max_length=1, choices=choices)
    item = models.ForeignKey(verbose_name='item', to='catalog.Item', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='User', to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
