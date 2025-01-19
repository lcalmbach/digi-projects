from django import template

register = template.Library()

@register.filter
def verbose_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name

@register.filter
def help_text(instance, field_name):
    return instance._meta.get_field(field_name).help_text

@register.filter
def to_range(value):
    """
    Converts a value to a range for iteration in templates.
    Usage: {% for i in 5|to_range %}
    """
    return range(value)