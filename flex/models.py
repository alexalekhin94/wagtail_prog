from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks


class FlexPage(Page):
     template = "flex/flex_page.html"

     content = StreamField(
         [
             ("title_and_text", blocks.TitleAndTextBlock()),
             ("full_richtext", blocks.RichtextBlock()),
             ("cards", blocks.CardBlock()) 
         ],

         null = True,
         blank = True 
     )
     
     subtitle = models.CharField(max_length=100, null=True, blank=True)

     content_panels= Page.content_panels + [
         FieldPanel("subtitle"),
         StreamFieldPanel("content"),

     ]

# Итак, для того, чтобы добавить StreamField в страницу, необходимо провернуть следующие шаги:
# 
# На нашей "гибкой странице" (по своей сути эта страница является своего рода конструктором, на котором происходит создание контента странцы),
# Добавляем блок с именем content, который как раз равен StreamField. Это поле может состоять из совершенно разных блоков, которые мы должны будем создать где-то
# Для этой цели создадим и подключим в base.py  приложение Streams при помощи команды python manage.py startapp streams. 
# В Streams создадим файл block.py, где и создадим все наши блоки. Например, мы можем унаследовать блок от blocks.StructBlock. Внутри блока задаем все поля, которые нам нужны внутри этого блока (естественно, нам нужно в шапке подтянуть block из wagtail.core)
# после чего указываем на этот блок в нашем коде models гибкой страницы. Также необходимо не забыть о задании template для StreamField.
# На "гибкой" странице вывод StreamField осуществляется посредством итерирования по блокам внутри {% for block in page.content %}{% include_block block %}{% endfor%}

