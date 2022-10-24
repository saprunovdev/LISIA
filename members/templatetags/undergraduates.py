from django import template
from members.models import Member

register = template.Library()

@register.inclusion_tag('members/tags/undergraduates.html', takes_context=True)
def undergraduates(context):
    return {
        'undergraduates': Member.objects.filter(rank="UN"),
        'request': context['request'],
    }