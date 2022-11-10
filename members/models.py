from django.db import models

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet
from professor.models import Professor

@register_snippet
class Member(models.Model):
    STATUS_CHOICES = (
        ('GR','Graduated'),
        ('ST', 'Studying'),
    )

    RANK_CHOICES = (
        ('PH', 'Ph.D'),
        ('MA', 'Master'),
        ('UN', 'Undergraduate'),
    )

    name = models.CharField(max_length = 20, blank=True)
    email = models.EmailField(max_length = 40, blank=True)
    status = models.CharField(max_length=2, choices = STATUS_CHOICES, blank=True)
    rank = models.CharField(max_length=2, choices = RANK_CHOICES, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete = models.SET_NULL,
        null = True,
        blank = False,
        related_name = '+',
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('status'),
        FieldPanel('rank'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "member"
        verbose_name_plural = "members"


class MembersPage(Page):
    max_count = 1
    template = "members/members_page.html"

    content_panels = Page.content_panels + [
        InlinePanel('members_list', label = 'members'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Add extra variables and return the updated context
        context['professor'] = Professor.objects.all()
        return context

    

class MembersToMembersPage(Orderable, models.Model):
    page = ParentalKey(
        'members.MembersPage',
        on_delete = models.CASCADE,
        related_name = 'members_list',
    )

    members_list = models.ForeignKey(
        'members.Member',
        on_delete = models.CASCADE,
        related_name = '+',
    )

    class Meta(Orderable.Meta):
        verbose_name = "members list"
        verbose_name_plural = "members lists"

    panels = [
        FieldPanel('members_list')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.members.name

class MembersToHomePage(Orderable, models.Model):
    page = ParentalKey(
        'home.HomePage',
        on_delete = models.CASCADE,
        related_name = 'members_list',
    )

    members_list = models.ForeignKey(
        'members.Member',
        on_delete = models.CASCADE,
        related_name = '+',
    )

    class Meta(Orderable.Meta):
        verbose_name = "members list"
        verbose_name_plural = "members lists"

    panels = [
        FieldPanel('members_list')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.members.name
