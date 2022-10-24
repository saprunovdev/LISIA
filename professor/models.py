from email.policy import default
from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet

@register_snippet
class Professor(models.Model):
    name = models.CharField(max_length = 20, blank=True)
    email = models.EmailField(max_length = 40, blank=True)
    affiliation = models.CharField(max_length = 300, blank=True)
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
        FieldPanel('affiliation'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "professor"
        verbose_name_plural = "professors"

class ProfessorsPage(Page):
    max_count = 1
    template = "professor/professors_page.html"

    professor_personal = RichTextField(default = "")
    professor_experience = RichTextField(default = "")
    professor_professional = RichTextField(default = "")

    content_panels = Page.content_panels + [
        InlinePanel('professor', label = 'professor'),
        FieldPanel('professor_personal'),
        FieldPanel('professor_experience'),
        FieldPanel('professor_professional'),
    ]

class ProfessorToProfessorsPage(Orderable, models.Model):
    page = ParentalKey(
        'professor.ProfessorsPage',
        on_delete = models.CASCADE,
        related_name = 'professor',
    )

    professor = models.ForeignKey(
        'professor.Professor',
        on_delete = models.CASCADE,
        related_name = '+',
    )

    class Meta(Orderable.Meta):
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

    panels = [
        FieldPanel('professor')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.members.name

class ProfessorToHomePage(Orderable, models.Model):
    page = ParentalKey(
        'home.HomePage',
        on_delete = models.CASCADE,
        related_name = 'professor',
    )

    professor = models.ForeignKey(
        'professor.Professor',
        on_delete = models.CASCADE,
        related_name = '+',
    )

    class Meta(Orderable.Meta):
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

    panels = [
        FieldPanel('professor')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.members.name