from django import template

register = template.Library()


@register.filter  # Собственный фильтр
def reverse_text(value):
    return value[::-1]


@register.simple_tag  # Собственный тег
def repeat_text(text, count):
    return text * count
