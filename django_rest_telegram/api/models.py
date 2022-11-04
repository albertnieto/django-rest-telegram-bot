from mongoengine import *


# Create your models here.
class Pole(Document):
    type = StringField(max_length=30)
    telegram_user_id = IntField()
    points = FloatField()
    date = DateField()
    date_time = DateTimeField()

class Coin(Document):
    name = StringField(max_length=30)
    telegram_user_id = IntField()
    date = DateField()

class TelegramUser(Document):
    telegram_id = IntField()
    is_bot = BooleanField()
    first_name = ListField(StringField(max_length=50))
    username = ListField(StringField(max_length=50))
    groups_id = ListField(StringField(max_length=30))
    #poles = ListField(EmbeddedDocumentField(Pole))
    #coins = ListField(EmbeddedDocumentField(Coin))

class TelegramGroup(Document):
    telegram_id = IntField()
    title = ListField(StringField(max_length=50))
    type = StringField(max_length=30)
