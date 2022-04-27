from django.core.validators import BaseValidator
from django.forms import ValidationError
from django.utils.html import strip_tags


def validate_brilliant(value: str):
    value = strip_tags(value)
    must_words = {'превосходно', 'роскошно'}
    if all(word not in value.lower() for word in must_words):
        raise ValidationError(f'Обязательно используйте слова {must_words}!')


class ValidateWordsCount(BaseValidator):
    def __init__(self, count):
        self.count = count
        super(BaseValidator, self).__init__()

    def __call__(self, value, *args, **kwargs):
        value = strip_tags(value)
        if len(str(value).split()) < self.count:
            raise ValidationError(f'Минимальное количество слов: {self.count}')
