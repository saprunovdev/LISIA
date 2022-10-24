from email.policy import default
from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Publication(models.Model):
    CATEGORY = (
        ("IN", "International"),
        ("DO", "Domestic"),
        ("PA", "Patents"),
    )

    authors = models.CharField(max_length = 200, blank=True)
    title = models.CharField(max_length = 400, blank=True)
    publication_date = models.DateField(blank = True, null = True)
    published_where = models.CharField(max_length = 400, blank=True)
    category = models.CharField(max_length=2, choices = CATEGORY, blank=True)

    panels = [
        FieldPanel('authors'),
        FieldPanel('title'),
        FieldPanel('publication_date'),
        FieldPanel('published_where'),
        FieldPanel('category'),
    ]

    def __str__(self):
        return self.title[:20]

    class Meta:
        verbose_name = "publication"
        verbose_name_plural = "publications"

class PublicationsPage(Page):
    max_count = 1
    template = "publications/publications_page.html"
