from mongoengine import *


# Create your models here.
class Pole(EmbeddedDocument):
    type = StringField(max_length=30)
    telegram_user_id = IntField()
    points = IntField()
    date_time = ComplexDateTimeField()

class Coin(EmbeddedDocument):
    name = StringField(max_length=30)
    date_time = ComplexDateTimeField()

class Telegram_User(Document):
    telegram_id = IntField()
    is_bot = BooleanField()
    first_name = ListField(StringField(max_length=50))
    username = ListField(StringField(max_length=50))
    groups_id = ListField(StringField(max_length=30))
    poles = ListField(EmbeddedDocumentField(Pole))
    coins = ListField(EmbeddedDocumentField(Coin))

class Telegram_Group(Document):
    telegram_id = IntField()
    title = ListField(StringField(max_length=50))
    type = StringField(max_length=30)
