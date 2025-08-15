# dashboard/templatetags/markdown_extras.py

import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='convert_markdown')
@stringfilter
def convert_markdown(value):
    # This function converts markdown text into safe HTML
    return mark_safe(markdown.markdown(value))