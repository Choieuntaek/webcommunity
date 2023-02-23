from django import template
import datetime
from django.utils import timezone

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def is_new(create_date):
    delta = create_date + datetime.timedelta(hours=24)
    if delta >= timezone.now():
        return "NEW"
    else:
        return ""