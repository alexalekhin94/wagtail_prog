from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import StreamField
from streams import blocks

from wagtail.core.models import Page

class BlogListPage(Page):

    template = "blog/blog_listing_page.html"

    custom_title = models.CharField(
        max_length=100,
        blank = False,
        null = False,
        help_text = 'Overwrites the default title'
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        return context

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]





class BlogDetailPage(Page):

    custom_title = models.CharField(
        max_length=100,
        blank = False,
        null = False,
        help_text = 'Overwrites the default title'
    )


    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank = True,
        null = True,
        related_name="+",
        on_delete = models.SET_NULL,

    )

    content = StreamField(
         [
             ("title_and_text", blocks.TitleAndTextBlock()),
             ("full_richtext", blocks.RichtextBlock()),
             ("cards", blocks.CardBlock()) 
         ],

         null = True,
         blank = True 
     )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content")
    ]

