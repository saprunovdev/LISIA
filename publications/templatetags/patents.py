from django import template
from publications.models import Publication

register = template.Library()

@register.inclusion_tag('publications/tags/patents.html', takes_context=True)
def patents(context):
    return {
        'patents': Publication.objects.filter(category="PA"),
        'request': context['request'],
    }