from django import template
from members.models import Member

register = template.Library()

@register.inclusion_tag('members/tags/masters.html', takes_context=True)
def masters(context):
    return {
        'masters': Member.objects.filter(rank="MA"),
        'request': context['request'],
    }