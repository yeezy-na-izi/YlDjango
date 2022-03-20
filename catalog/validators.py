from django.forms import ValidationError
from django.core.validators import BaseValidator


def validate_brilliant(value: str):
    must_word = {'превосходно', 'роскошно'}
    if not (must_word - (must_word - set(value.split()))):
        raise ValidationError(f'Обязательно используйте слова {must_word}!')


class ValidateWordsCount(BaseValidator):
    def __init__(self, count):
        self.count = count
        super(BaseValidator, self).__init__()

    def __call__(self, value, *args, **kwargs):
        if len(str(value).split()) < self.count:
            raise ValidationError(f'Минимальное количество слов - {self.count}')
