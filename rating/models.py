from django.contrib.auth.models import User
from django.db import models
from django.db.models.constraints import UniqueConstraint


class Rating(models.Model):
    choices = (
        (0, 'Нет оценки'),
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь'),
    )
    star = models.SmallIntegerField(
        verbose_name='Оценка',
        choices=choices,
        default=0
    )
    item = models.ForeignKey(
        verbose_name='Товар',
        to='catalog.Item',
        on_delete=models.CASCADE,
        related_name='item_stars'
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        constraints = [
            UniqueConstraint(fields=['item', 'user', ], name='unique_rating')
        ]

    def __str__(self):
        return f'{self.user} {self.item} {self.star}'
