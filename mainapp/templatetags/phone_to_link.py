from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def phone_to_link(value):
    return mark_safe(f"<a href='phoneto:{value}'>{value}</a>")
