from django import template
from members.models import Member

register = template.Library()

@register.inclusion_tag('members/tags/phds.html', takes_context=True)
def phds(context):
    return {
        'phds': Member.objects.filter(rank="PH"),
        'request': context['request'],
    }