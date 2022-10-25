from django import template
from publications.models import Publication

register = template.Library()

@register.inclusion_tag('publications/tags/international.html', takes_context=True)
def international(context):
    return {
        'international': Publication.objects.filter(category="IN"),
        'request': context['request'],
    }