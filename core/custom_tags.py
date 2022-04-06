from django import template

register = template.Library()


@register.filter(name='word_to')
def word_to(value: str, key: int):
    return ' '.join(value.split()[:key])
