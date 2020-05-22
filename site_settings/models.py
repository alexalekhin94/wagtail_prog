from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook=  models.URLField(blank=True, null = True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null = True, help_text="Twitter URL")
    youtube =  models.URLField(blank=True, null = True, help_text="Youtube URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel ("youtube"),
        ], heading = "Social Media Settings")
    ]   
        


    
# Урок 14. 
# Create your models here.
# Очень часто бывает необходимо определить глобальные настройки сайта (в примере с Ютуба это ссылки на на социальные сети итп). Было бы классно, если бы эти параметры можно было бы изменить прям из админки.
# Чтобы это провернуть сделаем следующее: с помощью команды python manage.py startapp {APP_NAME} создадим новое приложение,
# после чего добавим это приложение в настройки INSTALLED_APPS, которые расположены в файле base.py в папке с нашим проектом. По сути мы говорим приложению: "теперь юзаем это тоже".
# Создадим класс, куда поместим группу параметров, которые будем корректировать. Пример: twitter = models.URLField(), то есть параметр ссылки на социальную сеть.
# Далее добавим наши параметры в админку при помощи параметра panels. Чтобы там была не куча параметров, а структурированная панелька, это лучше сделать в следующем виде: panels = [MultiFieldPanel([ {All panels name}], heading = "Social Media Settings")].
# Важно не забыть импортировать в шапке обработичики поля: wagtail.contrib.settings.models import ....{nessesery fields} 
# Также добавим в шапку файла model.py в приложении site_settings (где мы и записали наш класс :)) wagtail.contrib.settings.models import BaseSettings, register-setting.
# По своей сути это декоратор, и нам нужно его указать перед нашим классом @register_setting.
#
# Если мы попробуем запустить сервер сейчас, то вылетит ошибка. Там будет говориться о том, wagailsettings не зарегистрировано в пространтве имен.
# Поэтому нам нужно вставить  'wagtail.contrib.settings.context_processor.settings' в файл base.py в раздел templates - options - context_processor
# После чего  в этом файле добавить 'wagtail.contrib.settings' в Installed_Apps
# Для того, чтобы использовать это на сайте воспользуемся следующей конструкцией:
# {{ settings.
#       site_settings.(то приложение, которые мы создалии)
#           SocialMediaSettings.(класс внутри приложения)
#                           facebook}}  (поле, из которого будет подтягиваться значение)
#
#
#
#
