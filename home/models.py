from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel

class HomePage(Page):
    max_count = 1
    template = "home/home_page.html"
    
    hero_title = models.CharField(max_length = 100, null = True)
    hero_body = models.CharField(max_length = 500, null = True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = "+"
    )


    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_body'),
        FieldPanel('hero_image'),
        InlinePanel('members_list', label = 'members'),
        InlinePanel('professor', label = 'professor'),
    ]