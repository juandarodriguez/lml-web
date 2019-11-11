from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, RichTextField

class LmlPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
