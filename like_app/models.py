from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# https://www.youtube.com/watch?v=fvcXyEUHh2c&list=PLrCZzMib1e9pg7ZLIOhmGSlmkMf8yEOLZ&index=6&t=4896s

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    item_type = models.ForeignKey(ContentType) # Превязанная модель, тип модели
    item_id = models.PositiveIntegerField() # ID экземпляра/объекта из бд
    item = GenericForeignKey("item_type", "item_id") # Привязанный объект
