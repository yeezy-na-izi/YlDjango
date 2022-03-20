from django.db import models
from catalog.validators import validate_brilliant, ValidateWordsCount


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

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'
