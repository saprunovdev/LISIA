from django import template
from publications.models import Publication

register = template.Library()

@register.inclusion_tag('publications/tags/domestic.html', takes_context=True)
def domestic(context):
    return {
        'domestic': Publication.objects.filter(category="DO"),
        'request': context['request'],
    }