import datetime

from django import template

register = template.Library()


@register.filter()
def price_format(value):
    return "{}  تومان".format(value)


@register.simple_tag()
def get_time(time_format):
    return datetime.datetime.now().strftime(time_format)
