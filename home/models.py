from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

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

    about_us_text = RichTextField(default = "", features=[
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'hr'
        ])

    about_us_image = models.ForeignKey(
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
        FieldPanel('about_us_text'),
        FieldPanel('about_us_image'),
        
        InlinePanel('publication', label = 'publication', max_num=3),
        InlinePanel('professor', label = 'professor', max_num=1),
        InlinePanel('members_list', label = 'member', max_num=4),     
    ]