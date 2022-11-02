from rest_framework_mongoengine import serializers
from drfTelegram.api.views import (
    Pole,
    Coin,
    Telegram_User,
    Telegram_Group,
)

class PoleSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Pole
        fields = [
            "type", "telegram_user_id", "points", "date_time",
        ]

class CoinSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Coin
        fields = [
            "name", "date_time",
        ]

class Telegram_UserSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Telegram_User
        fields = [
            "telegram_id",
            "is_bot", 
            "first_name",
            "username",
            "groups_id",
            "poles",
            "coins",
        ]

class Telegram_GroupSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Telegram_Group
        fields = [
            "telegram_id", "title", "type",
        ]