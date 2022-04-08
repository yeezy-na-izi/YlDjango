from django.core.validators import BaseValidator
from django.forms import ValidationError
from django.core.validators import BaseValidator


def validate_brilliant(value: str):
    must_words = {'превосходно', 'роскошно'}
    if len(must_words - set(value.split())) == len(must_words):
        raise ValidationError(f'Обязательно используйте слова {must_words}!')


class ValidateWordsCount(BaseValidator):
    def __init__(self, count):
        self.count = count
        super(BaseValidator, self).__init__()

    def __call__(self, value, *args, **kwargs):
        if len(str(value).split()) < self.count:
            raise ValidationError(f'Минимальное количество слов: {self.count}')
