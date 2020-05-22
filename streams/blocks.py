from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required = True, help_text = 'Add your title')
    text = blocks.TextBlock(required = True, help_text = 'Add additional text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon ="edit"
        label = "Title & Text"

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required = True, help_text = 'Add your title')
    cards = blocks.ListBlock(
    blocks.StructBlock(
        [
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=True)),
            ("text", blocks.TextBlock(required=True)),
            ("button_page", blocks.PageChooserBlock()), 
            ("button_url", blocks.URLBlock(required=False)),
        ]
    )
)

    class Meta:
        template = "streams/card_block.html"
        icon = "edit"
        label = "Card"


class RichtextBlock(blocks.RichTextBlock):
    

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"