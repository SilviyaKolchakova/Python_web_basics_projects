from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    """
    Capitalizes the value, i.e. makes the firs letter capital and lowers the rest

    *THIS is Text => This is text
    """
    return value[0].upper() + value[1:].lower()
