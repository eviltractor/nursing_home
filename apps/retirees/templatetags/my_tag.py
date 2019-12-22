import datetime

from django import template

register = template.Library()


@register.simple_tag(name='my_tag')
def my_tag():
    return f'{datetime.datetime.now()}'
