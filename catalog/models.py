from django.db import models


class Shelf(models.Model):
    class Meta:
        verbose_name = 'Полка'
        verbose_name_plural = 'Полки'

    name = models.CharField(verbose_name='Имя', max_length=128)
