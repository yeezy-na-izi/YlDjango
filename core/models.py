from django.db import models


class AbstractTag(models.Model):
    is_published = models.BooleanField(verbose_name='Опубликованно', default=True)
    slug = models.SlugField(verbose_name='slug', max_length=200, unique=True)

    class Meta:
        abstract = True
